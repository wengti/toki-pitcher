import { createClient } from "@/lib/supabase/server"
import CustomersHome from "./CustomersHome"

export default async function ContentHome() {

    try {

        /* Fetch Data from database */
        /* Sorted by Tenure End Date and Plan Name in ascending order */
        /* Only fetch those that have expired data after the current date */
        const now = new Date()
        const supabase = await createClient()
        const { data, error } = await supabase
            .from("customers")
            .select()
            .order('tenure_end', {ascending: true})
            .order('plan', {ascending: true})
            .gt('tenure_end', now.toISOString())
        if (error){
            throw new Error(error.message)
        }
        else if (data === null || data.length === 0){
            throw new Error("No valid data can be found.")
        }
        
        /* All the customer data are passed to the children component as props */
        return (
            <section className='min-h-(--content-h) flex flex-col'>
                <CustomersHome customersData={data}/>
            </section>
        )
    }
    catch (error) {
        const errorMessage = error instanceof Error 
            ? error.message
            : "An unknown error has occured"
        return (
            <section 
                className='min-h-(--content-h) flex flex-col items-center justify-center text-red-500 font-semibold text-2xl'
            >
                <p>Error: {errorMessage}</p>
                <p>Please contact the admin at wengti@hotmail.com.</p>
            </section>
        )
    }
}