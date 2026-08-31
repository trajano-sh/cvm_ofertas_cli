from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment

def export_csv_offers(data: dict):
    wb = Workbook()

    sheet = wb.active
    headers = ["ID", "NOME EMISSOR", "CNPJ EMISSOR", "NOME COORDENADOR LIDER", "CNPJ COORDENADOR LIDER",
        "TIPO REQUERIMENTO", "TIPO DE OFERTA", "STATUS", "NUMERO PROCESSO", "NUMERO REGISTROS", "VALOR EM REAIS",
        "POSSUI BOOK", "DATA", "LINK"]
    sheet.append(headers)


    header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for cell in sheet[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = header_alignment
    sheet.row_dimensions[1].height = 28
    link_font = Font(name="Calibri", size=11, color="0563C1", underline="single")
    print("Exporting...")
    for offer in data.get("registros", []):
        offer_id=offer.get("idRequerimento")
        url = f"https://web.cvm.gov.br/sre-publico-cvm/#/oferta-publica/{offer_id}"
        row = [offer.get("idRequerimento"), offer.get("nomeEmissor"), offer.get("cnpjEmissor"),
               offer.get("nomeCoordenadorLider"), offer.get("cnpjCoordenadorLider"), offer.get("nomeTipoRequerimento"),
               offer.get("nomeValorMobiliario"), offer.get("statusDaOferta"), offer.get("numeroProcesso"),
               offer.get("numeroRegistro"), offer.get("valorTotalEmReais"), offer.get("possuiBook"), offer.get("data"),
               "Link Oferta"]
        sheet.append(row)

        current_row=sheet.max_row
        link_cell = sheet[f"N{current_row}"]
        link_cell.hyperlink = url
        link_cell.font = link_font
        link_cell.alignment = Alignment(horizontal="center", vertical="center")

    for col in sheet.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        col_letter = col[0].column_letter
        sheet.column_dimensions[col_letter].width = max(max_len + 3, 10)
    sheet.freeze_panes = "A2"
    wb.save("offers.xlsx")
    print("Saved offers.xlsx")
