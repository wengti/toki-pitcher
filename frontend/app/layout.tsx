import type { Metadata } from "next";
import { Geist } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});


export const metadata: Metadata = {
    title: "Toki Pitcher",
    description: "An AI-powered application that helps broadband retention agent to generate personalized recontract pitches",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode; }>) {
    return (
        <html
            lang="en"
            className={`${geistSans.variable} h-full`}
        >
            <body className="bg-(--background-color) text-(--letter-white)">
                {children}
            </body>
        </html>
    );
}
