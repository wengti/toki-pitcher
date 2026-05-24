import Image from "next/image";

export default function Header(){

    return (
        <header 
            className='bg-(--header-color) flex justify-center items-center h-(--header-h)'
        >
            <Image 
                height={200}
                width={1040}
                alt="The logo of Toki Pitcher"
                src="/toki_banner.png"
                className='w-100'
            />
        </header>
    )
}