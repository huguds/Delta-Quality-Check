# Delta Quality Check

# Ferramentas
- Python (Pandas e Numpy) -> Consulta e tratamento dos dados

# 👷 Como rodar
```bash
# Clonar o repositório
git clone[ https://github.com/huguds/master-test.git](https://github.com/huguds/Delta-Quality-Check.git)
# Entrar numa IDE de sua preferência 
# Executar os seguintes comandos no terminal, caso não tenha as seguintes bibliotecas instaladas:
- pip install pandas
- pip install numpy
```

- **Observação**: Após a instalação das bibliotecas pode ser necessário, reiniciar a sua IDE para que ela atualize e assim, você consiga utilizar todos os comandos necessários para rodar o script.

## Informações sobre o Projeto

### Sobre o script de delta:

1. O script foi desenvolvido para auxiliar os profissionais que trabalham com dados, dessa forma o profissional precisara utilizar o seu próprio banco de dados e fazer a consulta diariamente.
2. A cada consulta, é necessário que o profissional baixe o resultado e coloque em uma pasta source, para que o script consiga identificar e ler os dados.
3. Após isso é necessário passar os caminhos de todos os arquivos que foram baixados, dessa forma:

![image](https://github.com/huguds/Delta-Quality-Check/assets/79457377/e6278877-ba97-4357-8b0b-233af825a331)

* **Observação**: Para que o script consiga executar da melhor forma possível, é necessário que as colunas estejam nesse formato:
![image](https://github.com/huguds/Delta-Quality-Check/assets/79457377/a48637d9-0be6-4547-b185-6cb735edd933)

### Resultado Final:

1. Após executar todo o script, você obterá um resultado parecido com este:

![image](https://github.com/huguds/Delta-Quality-Check/assets/79457377/dd9326a2-c0be-46a4-8f89-1b6719b08956)





