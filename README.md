# Sora Videos

Run the following script
```javascript
// Collect all links on the page
const links = Array.from(document.querySelectorAll('video'));

// Define the pattern to match
const pattern = /^https:\/\/videos\.openai\.com\/vg-assets\/assets(.*)/;

// Filter and print the matching links
const matchingLinks = links.map(link => link.src).filter(href => pattern.test(href));

console.log('Matching Links:', matchingLinks);
```

And then run `download.py`. The files will appear inside the downloads folder.

