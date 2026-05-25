'use client'

import { Database } from "@/types/supabase"
import React, { useState } from "react"
import { Toggle } from "../tailgrids/core/toggle"
import CustomerBox from "./CustomerBox"

export type CustomerType = Database["public"]["Tables"]["customers"]["Row"]

type CustomersHomePropsType = {
    customersData: CustomerType[]
}

export default function CustomersHome({ customersData }: CustomersHomePropsType) {

    const [isFiltered, setIsFiltered] = useState<boolean>(false)

    function handleFilter(event: React.ChangeEvent<HTMLInputElement>) {
        setIsFiltered(event.target.checked)
    }

    const now = new Date()
    const curYear = now.getFullYear()
    const curMonth = now.getMonth()


    const displayedCustomers = isFiltered
        ? customersData.filter((data) => {
            const endDate = new Date(data.tenure_end)
            const endYear = endDate.getFullYear()
            const endMonth = endDate.getMonth()
            return (endYear === curYear && endMonth === curMonth)
        })
        : customersData

    return (
        <>
            <div className='ml-auto mr-4 my-4'>
                <Toggle
                    label="Show contracts that expire this month"
                    checked={isFiltered}
                    onChange={handleFilter}
                />
            </div>
            <div className="grow gap-4 m-8 grid grid-cols-[repeat(auto-fill,minmax(300px,1fr))] md:grid-cols-[repeat(auto-fill,minmax(600px,1fr))]">
                {
                    displayedCustomers.map((data) =>
                        <CustomerBox customerData={data} key={data.id} />
                    )
                }
            </div>
        </>
    )
}