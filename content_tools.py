# Hand-written SEO content for the most-used tools. Others get a generated version.
CUSTOM = {
'image-upscaler': dict(
  intro="Make small, low-resolution or slightly blurry photos bigger and sharper. DoraPDF's AI upscaler (based on the ESRGAN super-resolution model) rebuilds fine detail as it enlarges your image 2× or 4× — far better than simply stretching it. Everything runs in your browser, so your photos stay on your device.",
  steps=["Drop a JPG, PNG, WebP or HEIC image.","Choose 2× or 4× and pick <b>AI</b> (best quality) or <b>Fast</b> (instant, classic + sharpen).","Press <b>Upscale</b>. The first time, the AI model downloads once (about 2 MB).","Drag the before/after slider to compare, then download your HD PNG."],
  faqs=[("How is AI upscaling different from resizing?","Normal resizing just stretches pixels, so the result looks soft. AI upscaling predicts the missing detail, giving sharper edges, cleaner text and more natural textures."),
        ("Why is it slow on my phone?","AI upscaling is heavy work done on your own device. Smaller images and 2× are fastest; for very large images use Fast mode."),
        ("What is the maximum size?","AI mode supports outputs up to about 6000 pixels on the long side. Fast mode works on any size.")]),
'object-remover': dict(
  intro="Remove unwanted objects, people, text, logos or blemishes from photos. Simply brush over what you want gone and DoraPDF fills the area using the surrounding pixels — no Photoshop skills needed, and your photo never leaves your device.",
  steps=["Upload your photo.","Paint over the object with the brush. Cover it completely and go slightly beyond its edges.","Press <b>Remove object</b>. Brush again over any leftovers and repeat for a cleaner result.","Download the cleaned image as PNG."],
  faqs=[("What works best?","Small and medium objects on simple backgrounds — wires, spots, text, people in the background, dates and logos. Very large objects on detailed backgrounds may need several passes."),
        ("Which fill style should I use?","Smooth works best for most photos. Try Natural when removing something that crosses straight lines or edges."),
        ("Is my photo uploaded?","No. The remover runs in your browser using OpenCV, so your photo stays private.")]),

'pdf-to-word': dict(
  intro="Convert any text-based PDF into an editable Microsoft Word (.docx) file in seconds. DoraPDF reads the text and headings from your PDF and rebuilds them in a Word document you can edit, copy and reformat — all inside your browser, so your file never leaves your device.",
  steps=["Drop your PDF into the box above, or click to choose it from your phone or computer.","Press <b>Convert now</b>. DoraPDF extracts the text, keeps headings bigger and bold, and adds page breaks between pages.","Download your .docx file and open it in Microsoft Word, Google Docs or WPS Office."],
  faqs=[("Will my formatting stay the same?","Text, paragraphs, headings and page breaks are kept. Complex layouts such as multi-column magazines or tables with merged cells may need a little touch-up in Word."),
        ("Can I convert a scanned PDF?","Scanned PDFs are pictures of text, so there is no text to extract yet. Run it through our PDF OCR tool first to make the text readable, then convert it to Word."),
        ("Is there a file size or page limit?","No hard limit. Because everything runs on your device, very large PDFs simply take a little longer on slower phones.")]),
'pdf-merger': dict(
  intro="Combine two or more PDF files into a single document. Add your files, arrange them in the order you want and merge them into one clean PDF — perfect for assignments, reports, invoices and scanned pages.",
  steps=["Add two or more PDF files. You can drop them all at once.","Remove any file you don't need with the ✕ button. Files are merged in the order shown.","Press <b>Merge PDFs</b> and download <i>merged.pdf</i>."],
  faqs=[("Does merging reduce quality?","No. Pages are copied exactly as they are — text stays selectable and images keep their original quality."),
        ("How many PDFs can I merge?","As many as your device can handle. Most phones merge dozens of files without any problem."),
        ("Can I merge password-protected PDFs?","Unlock them first with our Unlock PDF tool (you need the password), then merge.")]),
'pdf-compressor': dict(
  intro="Make PDF files smaller so they fit email limits and upload forms. Choose Smart mode to keep text selectable, or Strong mode to shrink image-heavy and scanned PDFs as much as possible.",
  steps=["Drop the PDF you want to shrink.","Choose <b>Smart</b> (keeps text) or <b>Strong</b> (maximum compression) and pick a quality level.","Press <b>Compress</b> — you'll see exactly how much smaller the new file is — then download it."],
  faqs=[("Which mode should I choose?","Use Smart for documents made in Word or exported from software. Use Strong for scanned pages and PDFs full of photos — it gives the biggest savings."),
        ("Why did my file barely shrink?","Some PDFs are already optimised. Try Strong mode with the Balanced or Smallest quality setting."),
        ("Is my document uploaded anywhere?","No. Compression happens entirely in your browser.")]),
'scan-to-pdf': dict(
  intro="Turn your phone into a document scanner — no app needed. Take photos of documents, receipts, notes or ID pages, drag the corners to crop and straighten them, apply a scan filter and save everything as one clean PDF.",
  steps=["Tap <b>Open camera</b> on your phone (or upload photos on a computer). Add as many pages as you like.","Drag the four pink corners to the edges of the paper — DoraPDF straightens the page automatically.","Pick a filter: Magic color, Black &amp; white, Grayscale or Lighten. Rotate if needed.","Choose page size and quality, then press <b>Download PDF</b>."],
  faqs=[("Do I need to install an app like CamScanner?","No. DoraPDF works in your phone's browser and does the same job: crop, straighten, enhance and export to PDF."),
        ("Which filter is best for documents?","Black &amp; white gives the sharpest text for printed pages. Magic color is best for receipts, forms and anything with colour."),
        ("Are my scans private?","Yes. Photos are processed on your phone and are never uploaded.")]),
'images-to-pdf': dict(
  intro="Combine JPG, PNG, WebP or iPhone HEIC photos into a single PDF. Each image becomes one page, in the order you add them — great for submitting assignments, receipts and photo documents.",
  steps=["Add your images. They become pages in the order shown.","Choose a page size (fit to image, A4 or US Letter) and a margin.","Press <b>Create PDF</b> and download your document."],
  faqs=[("Can I add iPhone HEIC photos?","Yes. HEIC photos are converted automatically before they are added to the PDF."),
        ("Will my photos lose quality?","Images are saved at high quality (around 92%) and scaled to a sharp print resolution."),
        ("Can I reorder pages?","Remove a file with ✕ and add it again to move it to the end, or add files in the order you want.")]),
'pdf-to-jpg': dict(
  intro="Export every page of a PDF as a high-quality JPG image. Ideal for sharing pages on WhatsApp or social media, adding them to slides, or using a page as a picture.",
  steps=["Drop your PDF.","Pick a quality level: Normal for screens, High for printing, Ultra for maximum sharpness.","Press <b>Convert</b>. Download pages one by one or all together as a ZIP."],
  faqs=[("Can I convert just one page?","Convert the PDF, then download only the page you need from the list."),("What resolution are the images?","High quality renders at about 180 DPI and Ultra at about 290 DPI — sharp enough for print.")]),
'word-to-pdf': dict(
  intro="Convert Word documents (.docx) to PDF so they look the same on every device. Text, headings, lists, tables and images are kept and laid out on A4 pages.",
  steps=["Drop your .docx file.","Press <b>Convert</b> — DoraPDF lays out the document on A4 pages.","Download your PDF, ready to share, print or submit."],
  faqs=[("Does it support old .doc files?","Please save the file as .docx first (File → Save As in Word)."),("Will my fonts change?","Common fonts are replaced with similar ones. For pixel-perfect output with special fonts, export directly from Word.")]),
'pdf-to-excel': dict(
  intro="Pull tables and text out of a PDF into an Excel spreadsheet (.xlsx). Each PDF page becomes its own sheet, with columns detected from the spacing in your document and numbers kept as real numbers.",
  steps=["Drop a text-based PDF (bank statements, price lists, reports).","Press <b>Convert</b>.","Download the .xlsx file and open it in Excel or Google Sheets."],
  faqs=[("Are numbers editable?","Yes — numbers are saved as numeric cells so you can sum and sort them."),("Does it work on scanned PDFs?","Scanned pages have no text layer. Run them through PDF OCR first, then convert to Excel.")]),
'pdf-splitter': dict(
  intro="Split a PDF into separate files or extract just the pages you need. Pull out a page range into a new PDF, or break every page into its own file.",
  steps=["Drop your PDF.","Choose <b>Extract pages</b> and type the pages (for example 1-3, 7), or choose <b>Split every page</b>.","Press <b>Split</b> and download your new PDF(s)."],
  faqs=[("How do I write page ranges?","Use commas and dashes: <i>1-3, 5, 8-10</i> extracts pages 1, 2, 3, 5, 8, 9 and 10."),("Is quality affected?","No, pages are copied exactly.")]),
'image-compressor': dict(
  intro="Reduce JPG, PNG and WebP image sizes for websites, email and uploads while keeping them looking sharp. Compress many images at once and see the savings for each file.",
  steps=["Add one or more images.","Choose a strength (Light, Balanced or Strong) and an optional maximum width.","Press <b>Compress</b> and download the smaller files."],
  faqs=[("How much smaller will my images be?","Typically 40–80% smaller with Balanced settings, depending on the photo."),("What happens to PNG files?","PNGs are converted to WebP, which keeps transparency and is much smaller.")]),
'qr-code-generator': dict(
  intro="Create free QR codes for website links, WiFi networks, WhatsApp chats and phone numbers. Customise the colours and download a high-resolution PNG for print or social media.",
  steps=["Choose the QR type: link, WiFi, WhatsApp or phone.","Enter your details and pick colours and size.","Download the PNG and test it with your phone camera."],
  faqs=[("Do these QR codes expire?","Never. They are static codes — the information is stored inside the code itself."),("Can people join my WiFi by scanning?","Yes. Choose WiFi, enter the network name and password, and guests can connect by scanning.")]),
'word-counter': dict(
  intro="Count words, characters, sentences and paragraphs instantly, and see how long your text takes to read or speak. Perfect for essays, assignments, social media captions and SEO writing.",
  steps=["Paste or type your text.","Counts update live as you type.","Use reading and speaking time to plan presentations."],
  faqs=[("Are spaces counted as characters?","Both are shown: characters with spaces and characters without spaces."),("Is my text saved?","No. Everything stays in your browser.")]),
'image-resizer': dict(
  intro="Resize images to exact pixel dimensions or by percentage. Keep the aspect ratio, convert format at the same time, and resize many photos in one go.",
  steps=["Add your images.","Enter a width and/or height in pixels, or switch to percentage.","Press <b>Resize</b> and download."],
  faqs=[("Will my image stretch?","Not if <i>Keep aspect ratio</i> is ticked — DoraPDF fits the image inside your size."),("What size is best for Instagram?","1080 × 1350 px for portrait posts and 1080 × 1080 px for square posts.")]),
'heic-to-jpg': dict(
  intro="Convert iPhone HEIC photos to universal JPG images that open everywhere — Windows, Android, websites and upload forms.",
  steps=["Add your HEIC photos.","Adjust quality if you like.","Press <b>Convert</b> and download your JPGs."],
  faqs=[("Why does my iPhone save HEIC?","HEIC saves space, but many websites and Windows PCs can't open it. JPG works everywhere."),("Can I convert many photos?","Yes, add as many as you want at once.")]),
'jpg-to-png': dict(
  intro="Convert JPG photos to PNG format for editing, design work and lossless saving.",
  steps=["Add your JPG images.","Press <b>Convert</b>.","Download the PNG files."],
  faqs=[("Does converting to PNG make the background transparent?","No — it changes the format only. Use our Image Background Remover to remove the background.")]),
'percentage-calculator': dict(
  intro="Solve every percentage question in one place: X% of a number, what percent one number is of another, and percentage increase or decrease.",
  steps=["Pick the calculator you need.","Enter your numbers.","The answer appears instantly."],
  faqs=[("How do I calculate a percentage increase?","Subtract the old value from the new value, divide by the old value and multiply by 100. The third calculator does it for you.")]),
'password-generator': dict(
  intro="Create strong, random passwords using your device's secure random generator. Choose the length and character types and see the password strength instantly.",
  steps=["Choose a length (16+ characters is recommended).","Select uppercase, lowercase, numbers and symbols.","Copy your new password and save it in a password manager."],
  faqs=[("Are generated passwords stored?","Never. They are created on your device and disappear when you leave the page.")]),
}
