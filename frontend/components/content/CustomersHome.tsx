'use client'

import { Database } from "@/types/supabase"
import { useState } from "react"

export type CustomerType = Database["public"]["Tables"]["customers"]["Row"]

type CustomersHomePropsType = {
    customersData: CustomerType[]
}

export default function CustomersHome({customersData}: CustomersHomePropsType){

    const [isFiltered, setIsFiltered] = useState<boolean>(false)
    const [displayedCustomer, setDisplayedCustomer] = useState<CustomerType[]>(customersData)

    return (
        <></>
    )
}