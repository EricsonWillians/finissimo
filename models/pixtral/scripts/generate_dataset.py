import json
import random
import os
import time
from dotenv import load_dotenv
import requests
from tqdm import tqdm

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

# Define constants
API_URL = "https://oyipiiu563qy4mqj.us-east-1.aws.endpoints.huggingface.cloud"
HEADERS = {
    "Accept": "application/json",
    "Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}",
    "Content-Type": "application/json"
}

# Ensure the output directory exists
output_dir = os.path.join(os.path.dirname(__file__), '..', 'dataset')
os.makedirs(output_dir, exist_ok=True)

# Define financial terms and concepts
financial_terms = [
    "PIX", "transferência bancária", "transferência eletrônica", "depósito bancário", 
    "investimento", "aplicação financeira", "taxa de juros", "juros compostos", 
    "conta corrente", "conta bancária", "conta poupança", "caderneta de poupança", 
    "cartão de crédito", "cartão de débito", "limite de crédito", "empréstimo", 
    "empréstimo pessoal", "empréstimo consignado", "financiamento", 
    "financiamento imobiliário", "financiamento de veículo", "taxa de câmbio", 
    "conversão de moeda", "criptoativos", "criptomoedas", "ativos digitais", 
    "ações", "mercado de ações", "mercado financeiro", "mercado de capitais", 
    "bolsa de valores", "índice da bolsa", "dividendos", "distribuição de lucros", 
    "rendimento", "retorno sobre investimento", "inflação", "desvalorização monetária", 
    "economia", "macroeconomia", "planejamento financeiro", "gestão financeira", 
    "educação financeira", "alfabetização financeira", "comprovante de pagamento", 
    "recibo de pagamento", "pagamento agendado", "agendamento de pagamento", 
    "pagamento efetuado", "pagamento concluído"
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

def query(payload):
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error querying the API: {e}")
        return [{"generated_text": "Não foi possível obter uma resposta detalhada no momento."}]

# Function to generate synthetic conversations in alpaca_chat format
def generate_conversations(n, terms, questions):
    data = []
    for _ in tqdm(range(n), desc="Generating conversations"):
        term = random.choice(terms)
        question_template = random.choice(questions)
        instruction = question_template.format(term=term)
        input_content = f"Como funciona o {term} no Brasil?"

        # Query the LLM for a detailed response
        response_payload = {"inputs": instruction}
        response = query(response_payload)

        # Extract the generated response
        generated_response = response[0].get("generated_text", "Não foi possível obter uma resposta detalhada no momento.")

        data.append({
            "instruction": instruction,
            "input": input_content,
            "response": generated_response
        })

        # Sleep to avoid overwhelming the endpoint
        time.sleep(1)  # Adjust the sleep time as needed
    return data

# Generate a dataset with a specified number of conversations
num_conversations = 1000

# Generate the dataset
synthetic_data = generate_conversations(num_conversations, financial_terms, questions)

# Save the dataset to a JSONL file in alpaca_chat format
output_file = os.path.join(output_dir, 'synthetic_financial_pix_dataset.jsonl')
with open(output_file, 'w', encoding='utf-8') as f:
    for entry in synthetic_data:
        json.dump(entry, f, ensure_ascii=False)
        f.write('\n')

print(f"Synthetic dataset with {num_conversations} financial conversations saved to {output_file}")
