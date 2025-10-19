import Link from "next/link";

export default async function About({searchParams, params}) {
    console.log(await searchParams);
    console.log(await params);
    return (
      <p>Hello Services</p>
    );
  }
  