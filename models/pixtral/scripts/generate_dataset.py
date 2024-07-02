import json
import random
import os
from datetime import datetime, timedelta

# Ensure the output directory exists
output_dir = 'models/pixtral/dataset'
os.makedirs(output_dir, exist_ok=True)

# Define financial terms and concepts
financial_terms = [
    "PIX",
    "transferência bancária",
    "transferência eletrônica",
    "depósito bancário",
    "investimento",
    "aplicação financeira",
    "taxa de juros",
    "juros compostos",
    "conta corrente",
    "conta bancária",
    "conta poupança",
    "caderneta de poupança",
    "cartão de crédito",
    "cartão de débito",
    "limite de crédito",
    "empréstimo",
    "empréstimo pessoal",
    "empréstimo consignado",
    "financiamento",
    "financiamento imobiliário",
    "financiamento de veículo",
    "taxa de câmbio",
    "conversão de moeda",
    "criptoativos",
    "criptomoedas",
    "ativos digitais",
    "ações",
    "mercado de ações",
    "mercado financeiro",
    "mercado de capitais",
    "bolsa de valores",
    "índice da bolsa",
    "dividendos",
    "distribuição de lucros",
    "rendimento",
    "retorno sobre investimento",
    "inflação",
    "desvalorização monetária",
    "economia",
    "macroeconomia",
    "planejamento financeiro",
    "gestão financeira",
    "educação financeira",
    "alfabetização financeira",
    "comprovante de pagamento",
    "recibo de pagamento",
    "pagamento agendado",
    "agendamento de pagamento",
    "pagamento efetuado",
    "pagamento concluído"
]

# Define question templates
questions = [
    "O que é {term} e qual a sua definição técnica no contexto financeiro?",
    "Como funciona o {term} no Brasil, incluindo seus processos e regulamentações?",
    "Quais são os benefícios do {term} em comparação com outros produtos financeiros disponíveis?",
    "Pode me explicar detalhadamente sobre {term}, incluindo suas principais características e funcionalidades?",
    "Como posso usar o {term} no meu banco para maximizar as vantagens financeiras e operacionais?",
    "Quais são os riscos associados ao {term} e quais estratégias posso adotar para mitigá-los?",
    "Qual é a melhor maneira de investir em {term}, considerando os diferentes perfis de investidores e objetivos financeiros?",
    "Como o {term} afeta a economia de maneira macroeconômica e microeconômica?",
    "Quais são as taxas envolvidas com {term} e como elas se comparam com outras taxas no mercado?",
    "Qual é a diferença entre {term} e outras opções financeiras, como outros tipos de contas, investimentos ou formas de pagamento?",
    "Como o {term} pode ajudar no meu planejamento financeiro, incluindo estratégias de curto, médio e longo prazo?",
    "Quais são as vantagens e desvantagens do {term} e como elas podem impactar minha decisão financeira?",
    "Como posso começar a usar {term}, incluindo os passos iniciais, requisitos e dicas práticas?",
    "Quais documentos são necessários para abrir uma {term} e quais são os procedimentos administrativos envolvidos?",
    "Como o {term} se compara com outras formas de pagamento em termos de custo, velocidade, segurança e aceitação?",
    "Qual é a taxa de rendimento média de um {term} e como essa taxa pode variar com o tempo e condições econômicas?",
    "Como posso monitorar minhas transações de {term} de forma eficiente, incluindo ferramentas e práticas recomendadas?",
    "Quais são as melhores práticas para usar {term} com segurança e evitar fraudes e outros riscos cibernéticos?",
    "O que preciso saber antes de investir em {term} para tomar uma decisão informada e estratégica?",
    "Como o {term} está regulamentado no Brasil, incluindo leis, normas do Banco Central e outras autoridades financeiras?",
    "Quais são as tendências futuras para {term} e como essas tendências podem impactar o mercado e os usuários?",
    "Como o {term} pode ser integrado com outras ferramentas financeiras para otimizar a gestão de recursos e investimentos?",
    "Quais são os erros comuns ao lidar com {term} e como posso evitá-los para garantir a eficiência e segurança?",
    "Qual é o impacto do {term} no planejamento de aposentadoria e em estratégias de longo prazo?",
    "Como a tecnologia está transformando o uso e a gestão de {term}, incluindo inovações recentes e futuras?",
    "Quais são os principais fatores a considerar ao escolher um {term} para investimentos, incluindo taxas, riscos e retornos?",
    "Como as mudanças econômicas, políticas e regulatórias afetam o desempenho e a segurança do {term}?",
    "Quais são os indicadores-chave para avaliar o desempenho de {term} e tomar decisões baseadas em dados?",
    "Como posso educar-me financeiramente para utilizar {term} de maneira mais eficaz e responsável?",
    "Quais são as implicações fiscais de investir ou utilizar {term}, incluindo tributação e deduções permitidas?",
    "Como o {term} pode ser usado para melhorar a liquidez e a gestão de fluxo de caixa pessoal ou empresarial?",
    "Quais são os impactos sociais e econômicos do uso disseminado de {term} em diferentes segmentos da população?",
    "Como o {term} interage com outras formas de crédito e financiamento, e como isso pode afetar minhas finanças pessoais?",
    "Quais são as opções de suporte e atendimento ao cliente para resolver problemas e tirar dúvidas sobre {term}?",
    "Como posso fazer uma comparação eficaz entre diferentes ofertas de {term} disponíveis no mercado?",
    "Quais são os casos de uso mais comuns para {term} em contextos pessoais e empresariais?",
    "Como o {term} se comporta em cenários de crise econômica e quais são as melhores estratégias nesses momentos?",
    "Quais são as barreiras de entrada para o uso de {term} e como superá-las?",
    "Como o uso de {term} pode influenciar minha pontuação de crédito e histórico financeiro?",
    "Quais são as principais inovações recentes em {term} e como elas podem beneficiar os usuários?",
    "Como o {term} pode ser utilizado para financiar grandes projetos pessoais, como compra de imóveis ou veículos?",
    "Quais são as políticas de privacidade e segurança associadas ao uso de {term}?",
    "Como posso personalizar o uso de {term} para atender às minhas necessidades financeiras específicas?",
    "Quais são os impactos do {term} no comércio eletrônico e nas transações digitais?",
    "Como o {term} pode ser usado para promover a inclusão financeira e bancarização de populações desassistidas?",
    "Quais são os principais desafios e oportunidades no uso de {term} em pequenas e médias empresas?",
    "Como o {term} pode ser parte de uma estratégia de diversificação de investimentos?",
    "Quais são os recursos educacionais disponíveis para aprender mais sobre {term}?"
]

def generate_conversations(n, terms, questions):
    data = []
    for _ in range(n):
        term = random.choice(terms)
        question = random.choice(questions).format(term=term)
        answer = f"O {term} é um conceito financeiro importante no Brasil. Ele é utilizado para diversas finalidades, incluindo {term.lower()}."

        # Add specific details for comprovantes de pagamento
        if "comprovante de pagamento" in term or "pagamento" in term:
            document_type = "PAGAMENTO" if "efetuado" in term else "AGENDADO"
            extraction_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%d/%m/%Y, %H:%M")
            document_number = f"DOC{random.randint(100000, 999999)}"
            issue_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%d/%m/%Y")
            due_date = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%d/%m/%Y")
            payment_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%d/%m/%Y") if document_type == "PAGAMENTO" else None
            bank_name = "Banco Exemplo"
            transaction_time = datetime.now().strftime("%H:%M:%S")
            transaction_code = f"TRANS{random.randint(1000, 9999)}"
            branch = f"{random.randint(100, 999)}"
            account_number = f"{random.randint(10000000, 99999999)}"
            transaction_type = random.choice(["Crédito", "Débito"])
            customer_name = "Nome Cliente"
            beneficiary_legal_name = "Nome Beneficiário"
            beneficiary_trade_name = "Nome Comercial Beneficiário"
            beneficiary_tax_id = f"{random.randint(10000000000, 99999999999)}"
            ultimate_beneficiary_name = "Nome Beneficiário Final"
            ultimate_beneficiary_tax_id = f"{random.randint(10000000000, 99999999999)}"
            payer_legal_name = "Nome Pagador"
            payer_tax_id = f"{random.randint(10000000000, 99999999999)}"
            payer_id = f"ID{random.randint(1000, 9999)}"
            invoice_amount = f"{random.uniform(100.0, 10000.0):.2f}"
            paid_amount = invoice_amount if document_type == "PAGAMENTO" else None
            payment_status = "Pago" if document_type == "PAGAMENTO" else "Agendado"
            notes = None
            document_url = "http://exemplo.com/documento.pdf"

            answer += (
                f" Este documento financeiro detalha uma transação do tipo {document_type}. Aqui estão os detalhes completos:\n"
                f"- Número do Documento: {document_number}\n"
                f"- Data de Emissão: {issue_date}\n"
                f"- Data de Vencimento: {due_date}\n"
                f"- Nome do Banco: {bank_name}\n"
                f"- Hora da Transação: {transaction_time}\n"
                f"- Código da Transação: {transaction_code}\n"
                f"- Agência Bancária: {branch}\n"
                f"- Número da Conta: {account_number}\n"
                f"- Tipo de Transação: {transaction_type}\n"
                f"- Nome do Cliente: {customer_name}\n"
                f"- Nome Legal do Beneficiário: {beneficiary_legal_name}\n"
                f"- Nome Comercial do Beneficiário: {beneficiary_trade_name}\n"
                f"- CPF/CNPJ do Beneficiário: {beneficiary_tax_id}\n"
                f"- Nome do Beneficiário Final: {ultimate_beneficiary_name}\n"
                f"- CPF/CNPJ do Beneficiário Final: {ultimate_beneficiary_tax_id}\n"
                f"- Nome Legal do Pagador: {payer_legal_name}\n"
                f"- CPF/CNPJ do Pagador: {payer_tax_id}\n"
                f"- ID do Pagador: {payer_id}\n"
                f"- Valor da Fatura: R$ {invoice_amount}\n"
                f"- Valor Pago: R$ {paid_amount if paid_amount else 'N/A'}\n"
                f"- Status do Pagamento: {payment_status}\n"
                f"- Notas: {notes}\n"
                f"- URL do Documento: {document_url}\n"
                f"Esses detalhes garantem a transparência e a rastreabilidade das transações financeiras, proporcionando segurança e confiança para todas as partes envolvidas."
            )

        data.append({"question": question, "answer": answer})
    return data

# Generate a dataset with a specified number of conversations
num_conversations = 1000
# Correctly pass the terms and questions to the function
synthetic_data = generate_conversations(num_conversations, financial_terms, questions)

# Save the dataset to a JSON file
output_file = 'models/pixtral/dataset/synthetic_financial_pix_dataset.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(synthetic_data, f, ensure_ascii=False, indent=4)

print(f"Synthetic dataset with {num_conversations} financial conversations saved to {output_file}")
