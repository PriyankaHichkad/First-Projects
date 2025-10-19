import Link from "next/link";
import { notFound } from "next/navigation";

export async function generateMetadata({params}) {
  const { FilePath } = await params;
  return {    
    title: `${FilePath}`,
    };
}

export default async function About({params}) {
    console.log(await params);
    const { FilePath } = await params;
    if(!/^\d+$/.test(FilePath)){
      notFound();
    }
    return (
      <div>File /{FilePath.join('/')}</div>
      //<p>File </p>
    );
  }
 