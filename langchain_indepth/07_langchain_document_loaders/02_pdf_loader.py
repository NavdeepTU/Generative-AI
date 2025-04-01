from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("temp.pdf")

docs = loader.load()

print(docs)

print(len(docs)) # 15 (because we have 15 pages in the pdf document)

print(docs[0].page_content)

print(docs[0].metadata)

# {'producer': 'pdfTeX-1.40.25',
#  'creator': 'LaTeX with hyperref',
#  'creationdate': '2024-04-10T21:11:43+00:00',
#  'author': '',
#  'keywords': '',
#  'moddate': '2024-04-10T21:11:43+00:00',
#  'ptex.fullbanner': 'This is pdfTeX, Version 3.141592653-2.6-1.40.25 (TeX Live 2023) kpathsea version 6.3.5',
#  'subject': '',
#  'title': '', 'trapped': '/False',
#  'source': 'temp.pdf',
#  'total_pages': 15,
#  'page': 0,
#  'page_label': '1'}