import { createClient } from "@/lib/supabase/server"

export default async function ContentHome() {

    try {

        const supabase = await createClient()
        const { data, error } = await supabase.from("customers").select()
        if (error){
            throw new Error(error.message)
        }
        else if (data === null || data.length === 0){
            throw new Error("No valid data can be found.")
        }
        
        return (
            <section className='min-h-(--content-h) flex flex-col'>
                <p>Hi</p>
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