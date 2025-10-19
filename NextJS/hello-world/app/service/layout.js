export const metadata = {
  title: 'Technical agency'
};

export default function Layout({children}) {
    return (
        <html lang="en">
        <body>
            <header style={{background: "red"}}> Header</header>
            <footer style={{background: "yellow"}}>Footer</footer>
          {children}
        </body>
      </html>
    );
  }