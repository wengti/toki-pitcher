'use client'

import { Database } from "@/types/supabase"
import React, { useState } from "react"
import { Toggle } from "../tailgrids/core/toggle"

export type CustomerType = Database["public"]["Tables"]["customers"]["Row"]

type CustomersHomePropsType = {
    customersData: CustomerType[]
}

export default function CustomersHome({ customersData }: CustomersHomePropsType) {

    const [isFiltered, setIsFiltered] = useState<boolean>(false)
    const [displayedCustomer, setDisplayedCustomer] = useState<CustomerType[]>(customersData)

    function handleFilter(event: React.ChangeEvent<HTMLInputElement>) {
        setIsFiltered(event.target.checked)
    }

    return (
        <>
            <div className='ml-auto mr-4 my-4'>
                <Toggle
                    label="Show contracts that expire this month"
                    checked={isFiltered}
                    onChange={handleFilter}
                />
            </div>
        </>
    )
}