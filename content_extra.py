# Extra SEO content for the most-searched tools: a tips section + extra FAQs.
# Keep every claim true to what the tool actually does.

EXTRA = {
 'pdf-to-word': {
  'tips': ('Tips for a clean PDF to Word conversion', [
   'Text-based PDFs (made from Word, Google Docs or a website) convert best, because the text is already inside the file.',
   'For a scanned PDF or a photo of a page, run <a href="/pdf-ocr/">PDF OCR</a> first so the text becomes readable, then convert.',
   'After converting, use Word\'s Styles panel to tidy headings in one click instead of fixing each line by hand.',
   'Need the exact look instead of editable text? Keep it as a PDF, or turn pages into images with <a href="/pdf-to-jpg/">PDF to JPG</a>.']),
  'faqs': [
   ('How do I convert a PDF to Word on my phone?', 'Open this page in Chrome or Safari on your phone, tap the box to pick your PDF, and download the .docx when it is ready. No app is needed.'),
   ('Can I open the converted file in Google Docs?', 'Yes. Upload the .docx to Google Drive and open it with Google Docs, or open it in Word, WPS or LibreOffice.'),
   ('Is it really free to convert PDF to Word?', 'Yes. There is no sign-up, no watermark and no daily limit.')]},
 'pdf-merger': {
  'tips': ('Tips for merging PDFs in the right order', [
   'Add files in the order you want them, then drag to rearrange before you merge.',
   'Name files with numbers first (01-cover, 02-report) so they line up correctly when you pick them.',
   'If a page is sideways, fix it first with <a href="/rotate-pdf/">Rotate PDF</a>.',
   'Merged file too big to email? Shrink it with <a href="/pdf-compressor/">Compress PDF</a>.']),
  'faqs': [
   ('How do I merge PDF files on my phone?', 'Open this page on your phone, pick the PDFs from your files, put them in order and tap merge. The combined PDF downloads to your phone.'),
   ('Is there a limit on how many PDFs I can merge?', 'There is no fixed limit. Very large batches depend on your device\'s memory, so merge in groups if a phone struggles.'),
   ('Can I merge PDFs with images?', 'Turn the images into a PDF first with <a href="/images-to-pdf/">Images to PDF</a>, then merge the files together.')]},
 'pdf-compressor': {
  'tips': ('How to get the smallest PDF', [
   'Scanned and photo-heavy PDFs shrink the most, because images take most of the space.',
   'PDFs that are mostly text are already small, so expect smaller savings there.',
   'Try Smart mode first. If the file is still too big for an upload form, try Strong mode.',
   'Remove pages you don\'t need with <a href="/delete-pdf-pages/">Delete PDF Pages</a> before compressing.']),
  'faqs': [
   ('How do I compress a PDF to under 1 MB or 500 KB?', 'Start with Strong mode, which works best on scans. If it is still too big, remove extra pages or split the file with <a href="/pdf-splitter/">Split PDF</a>.'),
   ('Will compressing make my PDF blurry?', 'Smart mode keeps text sharp. Strong mode lowers image quality to save more space, so check the result before sending.'),
   ('Can I compress a PDF on iPhone or Android?', 'Yes. It works in your phone\'s browser with no app.')]},
 'images-to-pdf': {
  'tips': ('Tips for turning photos into a neat PDF', [
   'Shoot pages in good light and hold the phone straight above the paper.',
   'For documents, <a href="/scan-to-pdf/">Scan to PDF</a> can crop and clean each page for a scanner-like look.',
   'Add pictures in page order, then rearrange if needed before creating the PDF.',
   'If the final PDF is large, run it through <a href="/pdf-compressor/">Compress PDF</a>.']),
  'faqs': [
   ('How do I convert a picture to PDF on iPhone?', 'Open this page in Safari, tap the box, choose your photos from the library, and create the PDF. HEIC photos are supported.'),
   ('How many images can I put in one PDF?', 'There is no fixed limit. Each image becomes one page.'),
   ('Can I convert JPG to PDF without losing quality?', 'Yes. Images are placed into the PDF without being shrunk unless you choose to.')]},
 'scan-to-pdf': {
  'tips': ('How to get scanner-quality results from your phone', [
   'Put the paper on a dark, plain surface so the edges are easy to find.',
   'Use daylight or a bright room and avoid your own shadow over the page.',
   'Drag the corners right to the paper edges for a straight, flat page.',
   'Use the black-and-white filter for text documents and colour for photos or stamps.']),
  'faqs': [
   ('Is this a free CamScanner alternative?', 'Yes. You can scan, crop, clean and save multi-page PDFs for free in your browser, with no app or watermark.'),
   ('How many pages can I scan?', 'As many as you need. All pages go into one PDF.'),
   ('Can I scan on a laptop?', 'Yes. Pick photos of your pages that are already on your computer, and crop and clean them the same way.')]},
 'pdf-to-jpg': {
  'tips': ('Tips for converting PDF pages to images', [
   'Choose a higher quality if you plan to print the images or zoom in.',
   'Need transparent or lossless images? Use <a href="/pdf-to-png/">PDF to PNG</a> instead.',
   'Only need the pictures inside a PDF, not whole pages? Use <a href="/pdf-image-extractor/">PDF Image Extractor</a>.']),
  'faqs': [
   ('How do I convert a PDF to JPG on my phone?', 'Open this page on your phone, pick the PDF and download the images. Every page becomes its own JPG.'),
   ('Can I convert just one page?', 'Yes. Convert the PDF and keep only the pages you need, or split it first with <a href="/pdf-splitter/">Split PDF</a>.')]},
 'word-to-pdf': {
  'tips': ('Tips for converting Word to PDF', [
   'Check fonts before converting. Common fonts like Calibri, Arial and Times New Roman give the most reliable results.',
   'Turn track changes off and accept edits first, so comments don\'t appear in the PDF.',
   'Converting several documents? Convert each one, then join them with <a href="/pdf-merger/">Merge PDF</a>.']),
  'faqs': [
   ('How do I convert Word to PDF on my phone?', 'Open this page on your phone, choose the .docx from your files and download the PDF.'),
   ('Does it work with .doc files?', 'It works best with .docx. Save an old .doc file as .docx in Word or Google Docs first.')]},
 'pdf-to-excel': {
  'tips': ('Tips for getting tables from PDF into Excel', [
   'Text-based PDFs with clear table lines convert best.',
   'For scanned bank statements or invoices, run <a href="/pdf-ocr/">PDF OCR</a> first.',
   'After converting, check that numbers are stored as numbers in Excel so formulas work.']),
  'faqs': [
   ('Can I open the result in Google Sheets?', 'Yes. Upload the .xlsx to Google Drive and open it with Google Sheets.'),
   ('Does it work for bank statements?', 'It works for text-based statements. Always double-check the numbers against the original.')]},
 'image-compressor': {
  'tips': ('Tips for compressing images without visible quality loss', [
   'JPG and WebP shrink the most. PNG is best kept for logos and screenshots.',
   'Resize very large photos with <a href="/image-resizer/">Image Resizer</a> first. Fewer pixels means a much smaller file.',
   'For websites, converting to WebP with <a href="/png-to-webp/">PNG to WebP</a> often halves the size.']),
  'faqs': [
   ('How do I reduce an image to under 100 KB or 50 KB?', 'Lower the quality setting a little at a time and resize the image if needed. Most photos reach 100 KB at a normal screen size.'),
   ('Can I compress many images at once?', 'Yes. Add several images and download each compressed file.')]},
 'pdf-splitter': {
  'tips': ('Tips for splitting PDFs', [
   'Use page ranges like 1-3, 5, 8-10 to pull out exactly the pages you need.',
   'To remove a few pages instead, <a href="/delete-pdf-pages/">Delete PDF Pages</a> is faster.',
   'Split a large PDF into parts to get under email or upload size limits.']),
  'faqs': [
   ('How do I extract one page from a PDF?', 'Enter just that page number and download it as a new PDF.'),
   ('Can I split a PDF on my phone?', 'Yes. It works in any phone browser.')]},
 'heic-to-jpg': {
  'tips': ('Why convert HEIC to JPG?', [
   'iPhones save photos as HEIC, which many Windows apps, websites and upload forms don\'t accept.',
   'JPG opens everywhere: Windows, Android, WhatsApp, email and online forms.',
   'Want the photos in one document? Use <a href="/heic-to-pdf/">HEIC to PDF</a>.']),
  'faqs': [
   ('How do I open HEIC files on Windows?', 'Convert them to JPG here, then open them with any photo viewer.'),
   ('Can I convert many HEIC photos at once?', 'Yes. Pick several photos and download each JPG.')]},
 'image-background-remover': {
  'tips': ('Tips for a clean background removal', [
   'Photos with a clear subject and good contrast against the background give the cleanest edges.',
   'Download as PNG to keep the transparent background.',
   'Use the result for product photos, profile pictures, stickers and presentations.']),
  'faqs': [
   ('Why is the first removal slow?', 'The AI model downloads to your browser once. After that, removals are much faster.'),
   ('Can I add a white background instead?', 'Yes. Place the transparent PNG on a white background in any editor, or use it as it is in documents and slides.')]},
}
