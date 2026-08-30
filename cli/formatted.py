from typing import Dict, Any, List

def format_offers_table(data: Dict[str, Any]) -> None:
    offers: List[Dict[str, Any]] = data.get("registros", [])
    if not offers:
        print("\nNenhuma oferta encontrada para o período informado.\n")
        return

    total_registros = data.get("totalRegistros", len(offers))
    print(f"\nTotal de registros encontrados: {total_registros}")
    print("-" * 180)
    print(f"{'ID':<8} | {'EMISSOR':<35} | {'VALOR (R$)':<15} | {'SITUAÇÃO':20} | {'TIPO':15} | {'TIPO REQUERIMENTO':30}")
    print("-" * 180)

    for item in offers:
        offer_id = str(item.get("idRequerimento", "N/A"))
        emissor = str(item.get("nomeEmissor", "Não informado"))[:33]
        
        raw_valor = item.get("valorTotalEmReais", "0")
        valor = parse_brl_to_float(raw_valor)
        
        situacao = str(item.get("statusDaOferta", "N/A"))[:20]
        tipo = str(item.get("nomeValorMobiliario", "N/A"))[:15]
        qualifiquedOrProfessional = str(item.get("nomeTipoRequerimento"))
        print(f"{offer_id:<8} | {emissor:<35} | {valor:>15,.2f} | {situacao:<20} | {tipo:<15} | {qualifiquedOrProfessional:<30}")
    print("-" * 180 + "\n")

def parse_brl_to_float(val_str: str) -> float:
    if not val_str or not isinstance(val_str, str):
        return 0.0
    clean_val = val_str.replace(".", "").replace(",", ".")
    try:
        return float(clean_val)
    except ValueError:
        return 0.0

def format_get_offer(data: Dict[str, Any],id:int) -> None:
    print(f"Processo: {data.get("numeroProcesso")}")
    print(f"Tipo de Oferta: {data.get("nomeValorMobiliario")}")
    print(f"Valor: {data.get("valorTotal")}")
    print(f"Data: {data.get("data")}")
    print(f"link: https://web.cvm.gov.br/sre-publico-cvm/#/oferta-publica/{id}")
