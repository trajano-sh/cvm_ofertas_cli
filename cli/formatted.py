from typing import Dict, Any, List

def format_offers_table(data: Dict[str, Any]) -> None:
    offers: List[Dict[str, Any]] = data.get("registros", [])
    if not offers:
        print("\nNenhuma oferta encontrada para o período informado.\n")
        return

    total_registros = data.get("totalRegistros", len(offers))
    print(f"\nTotal de registros encontrados: {total_registros}")
    print("-" * 80)
    print(f"{'ID':<10} | {'EMISSOR':<35} | {'VALOR (R$)':<15} | {'SITUAÇÃO'}")
    print("-" * 80)

    for item in offers:
        offer_id = str(item.get("idRequerimento", "N/A"))
        emissor = str(item.get("nomeEmissor", "Não informado"))[:33] # trunca se for longo
        valor = str(item.get("valorTotalEmReais", "0,00"))
        situacao = item.get("statusDaOferta", "N/A")

        print(f"{offer_id:<10} | {emissor:<35} | {valor:>12,.2f} | {situacao}")

    print("-" * 80 + "\n")