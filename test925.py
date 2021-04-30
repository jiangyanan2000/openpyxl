from docxtpl import DocxTemplate,RichText


tpl = DocxTemplate("13.docx")
rt = RichText("an exemple of ")
rt.add("a rich text",style="yangshi")
context = {
    'example': rt,
}

tpl.render(context)
tpl.save("13.docx")
