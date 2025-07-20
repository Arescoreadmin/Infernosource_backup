"use client";
import { useEffect, useState } from "react";

export default function SitesPages() {
  const [pages, setPages] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/sites/pages')
      .then(res => res.json())
      .then(data => setPages(data));
  }, []);

  return (
    <div>
      <h2>Sites & Pages</h2>
      <pre>{JSON.stringify(pages, null, 2)}</pre>
      <h3>List of Pages</h3>
      <ul>
        {pages.map((page, idx) => (
          <li key={page.url ?? idx} style={{marginBottom: "1rem"}}>
            <strong>URL:</strong> {page.url} <br />
            <strong>Extracted Text:</strong> {page.extracted_text}
          </li>
        ))}
      </ul>
    </div>
  );
}
