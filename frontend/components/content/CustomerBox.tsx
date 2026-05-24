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

    async function handleCopy() {
        try {
            await navigator.clipboard.writeText(pitchVal);
        } catch (error) {
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
                        <p>{monthly_usage}</p>
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
            <div className="flex gap-4 mt-8 justify-around">
                <button
                    className='bg-(--header-color) p-2 rounded-lg hover:opacity-50 active:opacity-50 cursor-pointer'
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
                pitchVal &&
                <div className='py-4 font-normal'>
                    <p className="text-(--letter-pink) text-sm font-bold">Generated Pitch: </p>
                    <p>{pitchVal}</p>
                </div>
            }

        </div>
    )
}