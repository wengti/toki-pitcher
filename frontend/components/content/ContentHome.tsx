import { createClient } from "@/lib/supabase/server"
import CustomersHome from "./CustomersHome"

export default async function ContentHome() {

    try {

        const now = new Date()

        const supabase = await createClient()
        const { data, error } = await supabase
            .from("customers")
            .select()
            .order('tenure_end', {ascending: true})
            .gt('tenure_end', now.toISOString())
        if (error){
            throw new Error(error.message)
        }
        else if (data === null || data.length === 0){
            throw new Error("No valid data can be found.")
        }
        
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