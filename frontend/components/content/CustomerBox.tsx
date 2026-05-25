'use client'

import { useState } from "react"
import { CustomerType } from "./CustomersHome"

type CustomerBoxPropsType = {
    customerData: CustomerType
}

export default function CustomerBox({ customerData }: CustomerBoxPropsType) {

    const { name, plan, monthly_usage, tenure_start, tenure_end, pitch: originalPitchVal } = customerData

    const [pitchVal, setPitchVal] = useState<string>(originalPitchVal)
    const [error, setError] = useState<Error | null>(null)
    const [isLoading, setIsLoading] = useState<boolean>(false)
    const [isPitchShown, setIsPitchShown] = useState<boolean>(false)

    async function handleCopy() {
        try {
            await navigator.clipboard.writeText(pitchVal)
        } catch (error) {
            if (error instanceof Error) setError(new Error(error.message))
            else setError(new Error("An unknown error has occured. Please try again."))
        }
    }

    async function generatePitch() {
        try {
            setError(null)
            setIsLoading(true)

            const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL!}/pitch`, {
                method: "POST",
                body: JSON.stringify(customerData),
                headers: {
                    "Content-Type": "application/json"
                }
            })

            // Improve the error message based on server error
            if (!res.ok) {
                const errorData = await res.json()
                throw new Error(errorData["detail"])
            }

            const data = await res.json()

            // Verify if this is working
            if (data.new_pitch_val) {
                setPitchVal(data.new_pitch_val)
            }
            setIsLoading(false)
            setIsPitchShown(true)

        } catch (error) {
            setIsLoading(false)
            if (error instanceof Error) setError(new Error(error.message))
            else setError(new Error("An unknown error has occured. Please try again."))
        }
    }


    return (
        <div className='border border-white rounded-2xl font-bold p-4 flex flex-col relative'>
            <div className="flex flex-col gap-4 text-xl justify-center">
                <div>
                    <p className='text-xs text-(--letter-pink)'>Name: </p>
                    <p>{name}</p>
                </div>
                <div className="flex gap-4 w-full">
                    <div className='w-1/2'>
                        <p className='text-xs text-(--letter-pink)'>Plan: </p>
                        <p>{plan}</p>
                    </div>
                    <div>
                        <p className='text-xs text-(--letter-pink)'>Monthly Usage: </p>
                        <p>{monthly_usage} GB</p>
                    </div>
                </div>
                <div className="flex gap-4">
                    <div className='w-1/2'>
                        <p className='text-xs text-(--letter-pink)'>Tenure Start: </p>
                        <p>{tenure_start}</p>
                    </div>
                    <div>
                        <p className='text-xs text-(--letter-pink)'>Tenure End: </p>
                        <p>{tenure_end}</p>
                    </div>
                </div>
            </div>
            <div className="flex gap-4 mt-8 justify-around md:justify-start">
                <button
                    className='bg-(--header-color) p-2 rounded-lg hover:opacity-50 active:opacity-50 cursor-pointer'
                    onClick={() => generatePitch()}
                >
                    Generate Pitch
                </button>
                <button
                    className='bg-(--header-color) p-2 rounded-lg hover:opacity-50 active:opacity-50 cursor-pointer'
                    onClick={() => { handleCopy() }}
                >
                    Copy Pitch
                </button>
            </div>
            {
                error &&
                <div>
                    <p className="text-red-500 text-sm font-normal">
                        {error.message}
                    </p>
                </div>
            }
            {
                isLoading &&
                <div>
                    <p className="text-sm font-normal">
                        Generating...
                    </p>
                </div>
            }
            {
                pitchVal &&
                <div className='py-4 font-normal'>
                    <p 
                        className="text-(--letter-pink) text-sm font-bold underline cursor-pointer hover:text-(--letter-white) active:text-(--letter-white)"
                        onClick={() => {setIsPitchShown((curVal) => !curVal)}}
                    >
                        {isPitchShown ? "Hide Generated Pitch": "Show Generated Pitch"} 
                    </p>
                    {
                        isPitchShown &&
                        <p className="whitespace-pre-wrap">{pitchVal}</p>
                    }
                </div>
            }

        </div>
    )
}