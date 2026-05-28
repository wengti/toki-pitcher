'use client'

import { Database } from "@/types/supabase"
import React, { useState } from "react"
import { Toggle } from "../tailgrids/core/toggle"
import CustomerBox from "./CustomerBox"

/* Type */
export type CustomerType = Database["public"]["Tables"]["customers"]["Row"]

type CustomersHomePropsType = {
    customersData: CustomerType[]
}

/* Component */
export default function CustomersHome({ customersData }: CustomersHomePropsType) {


    /* Filtering logic */
    /* When the toggle is turned on, it filters out the customer that has contract that expires this month */
    const [isFiltered, setIsFiltered] = useState<boolean>(false)

    function handleFilter(event: React.ChangeEvent<HTMLInputElement>) {
        setIsFiltered(event.target.checked)
    }

    const now = new Date()
    const curDate = now.getDate()
    const curMonth = curDate > 28 ? now.getMonth() + 1 : now.getMonth()
    const modCurMonth = curMonth % 12
    const curYear = curMonth > 11 ? now.getFullYear() + 1 : now.getFullYear()


    const displayedCustomers = isFiltered
        ? customersData.filter((data) => {
            const endDate = new Date(data.tenure_end)
            const endMonth = endDate.getMonth()
            const endYear = endDate.getFullYear()
            return (endYear === curYear && endMonth === modCurMonth)
        })
        : customersData

    return (
        <>
            {/* The Filter Component */}
            <div className='ml-auto mr-4 my-4'>
                <Toggle
                    label="Show contracts that expire this month"
                    checked={isFiltered}
                    onChange={handleFilter}
                />
            </div>

            {/* The Grid that holds all customers data */}
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