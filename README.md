# Delta-Quality-Check
This is a script to check Delta quality in list paths

# Principais ferramentas utilizadas na Engenharia de Dados

A area de Engenharia de Dados tem se destacado cada vez mais no mercado de trabalho, apresentando um crescimento significativo nos últimos anos. E a cada ano surge uma nova ferramenta que pode auxiliar e muito o Engenheiro(a) de Dados em seu trabalho.
Quando falamos sobre Engenharia de Dados, muito se fala sobre ETL e Pipeline de Dados, mas a final o que seria isso? <br><br>
ETL é a abreviação do termo (Extraction, Transform e Loading), ou seja extração, tratamento/transformação e o carregamento do dados para um local seguro, onde posteriormente ele possa ser consumido.

Muitas pessoas confundem Pipeline de dados com ETL, mas na verdade, ETL é somente uma parte do Pipeline de dados.

Pipeline de dados além de conter uma parte de ETL, também contém o enriquecimento dos dados, dependendo da base que está sendo consumida é necessário cruzar N bases diferentes para conseguir chegar no resultado necessário, o dado precisa passar por diferentes camadas até chegar na camada final.

Dado essa explicação, podemos citar as ferramentas que mais são utilizadas no processo de ETL em Engenharia de Dados.

Vale lembrar que não tem uma ordem especifica e sim aquele que mais se adequa ao caso de uso

* Extraction:

    **Stitch**: É ferramenta de integração de dados, onde só é necessário configurar a origem e o destino de onde os dados serão extráidos e salvos, também é possível programar um horário para que seja realizada a ingestão dos dados diariamente. Por ser um processo automático existe um custo e um limite que varia de acordo com o plano do serviço contratado.

    **AWS Glue**: É um serviço gerenciado de ETL da Amazon Web Services (AWS). Ele permite a extração, transformação e carregamento de dados de fontes diversas para armazenamentos de dados na nuvem.

    **NIFI**: É uma ferramenta open-source de ETL desenvolvida pela **apache** e não possui um custo, ou seja pode ser utilizada de maneira gratuita. Com essa ferramenta é possível fazer a extração de grande quantidade de dados sem precisar criar nenhuma linha de código, pois existem **processors** que são responsáveis por executar diversas funções.

    **Talend**: É Uma ferramenta completa de integração de dados que unifica todas as operações de dados, como: integração de dados, governança, qualidade de dados e integrações com diversas APIs.

    **Pentaho Data Integration (Kettle)**: uma ferramenta open-source de ETL que oferece recursos avançados para extração de dados. Nesse caso também não é necessário utilizar código, pois existem steps especificos que possuem diversas funções e pode ser adicionando ao fluxo de dados.

* Transformação (Transform):

    **Spark**: É uma ferramenta de processamento de dados em larga escala, com suporte a stream processing, batch processing e machine learning. É muito utilizado para a etapa de transformação dos dados.
    
    **Dataflow**: É uma ferramenta de processamento de dados em larga escala da Google, que permite a execução de pipelines ETL de maneira escalável e gerenciada.

    **Kafka Streams**: Uma biblioteca de processamento de streams do Apache Kafka que permite transformações em tempo real.

    **Airflow**: Uma plataforma de orquestração de fluxos de trabalho que pode ser usada para transformar e processar dados.

* Carregamento (Loading):

    **Redshift**: É um serviço de data warehouse gerenciado pela AWS, utilizado para o armazenamento e processamento de grandes volumes de dados.

    **BigQuery**: É um serviço de data warehouse gerenciado pela Google, que permite o armazenamento e processamento de grandes volumes de dados de forma escalável e eficiente.

    **Azure Synapse Analytics**: Um serviço de data warehouse gerenciado da Microsoft.

    **Snowflake**: Uma plataforma de data warehouse na nuvem que oferece escalabilidade e desempenho.
    
    **Amazon S3**: O serviço de armazenamento de objetos da AWS, muito utilizado para carregar dados em bruto

A seguir encontra-se um exemplo de ETL e Pipeline de dados:

# Principais ferramentas utilizadas na Engenharia de Dados

A area de Engenharia de Dados tem se destacado cada vez mais no mercado de trabalho, apresentando um crescimento significativo nos últimos anos. E a cada ano surge uma nova ferramenta que pode auxiliar e muito o Engenheiro(a) de Dados em seu trabalho.
Quando falamos sobre Engenharia de Dados, muito se fala sobre ETL e Pipeline de Dados, mas a final o que seria isso? <br><br>
ETL é a abreviação do termo (Extraction, Transform e Loading), ou seja extração, tratamento/transformação e o carregamento do dados para um local seguro, onde posteriormente ele possa ser consumido.

Muitas pessoas confundem Pipeline de dados com ETL, mas na verdade, ETL é somente uma parte do Pipeline de dados.

Pipeline de dados além de conter uma parte de ETL, também contém o enriquecimento dos dados, dependendo da base que está sendo consumida é necessário cruzar N bases diferentes para conseguir chegar no resultado necessário, o dado precisa passar por diferentes camadas até chegar na camada final.

Dado essa explicação, podemos citar as ferramentas que mais são utilizadas no processo de ETL em Engenharia de Dados.

Vale lembrar que não tem uma ordem especifica e sim aquele que mais se adequa ao caso de uso

* Extraction:

    **Stitch**: É ferramenta de integração de dados, onde só é necessário configurar a origem e o destino de onde os dados serão extráidos e salvos, também é possível programar um horário para que seja realizada a ingestão dos dados diariamente. Por ser um processo automático existe um custo e um limite que varia de acordo com o plano do serviço contratado.

    **AWS Glue**: É um serviço gerenciado de ETL da Amazon Web Services (AWS). Ele permite a extração, transformação e carregamento de dados de fontes diversas para armazenamentos de dados na nuvem.

    **NIFI**: É uma ferramenta open-source de ETL desenvolvida pela **apache** e não possui um custo, ou seja pode ser utilizada de maneira gratuita. Com essa ferramenta é possível fazer a extração de grande quantidade de dados sem precisar criar nenhuma linha de código, pois existem **processors** que são responsáveis por executar diversas funções.

    **Talend**: É Uma ferramenta completa de integração de dados que unifica todas as operações de dados, como: integração de dados, governança, qualidade de dados e integrações com diversas APIs.

    **Pentaho Data Integration (Kettle)**: uma ferramenta open-source de ETL que oferece recursos avançados para extração de dados. Nesse caso também não é necessário utilizar código, pois existem steps especificos que possuem diversas funções e pode ser adicionando ao fluxo de dados.

* Transformação (Transform):

    **Spark**: É uma ferramenta de processamento de dados em larga escala, com suporte a stream processing, batch processing e machine learning. É muito utilizado para a etapa de transformação dos dados.
    
    **Dataflow**: É uma ferramenta de processamento de dados em larga escala da Google, que permite a execução de pipelines ETL de maneira escalável e gerenciada.

    **Kafka Streams**: Uma biblioteca de processamento de streams do Apache Kafka que permite transformações em tempo real.

    **Airflow**: Uma plataforma de orquestração de fluxos de trabalho que pode ser usada para transformar e processar dados.

* Carregamento (Loading):

    **Redshift**: É um serviço de data warehouse gerenciado pela AWS, utilizado para o armazenamento e processamento de grandes volumes de dados.

    **BigQuery**: É um serviço de data warehouse gerenciado pela Google, que permite o armazenamento e processamento de grandes volumes de dados de forma escalável e eficiente.

    **Azure Synapse Analytics**: Um serviço de data warehouse gerenciado da Microsoft.

    **Snowflake**: Uma plataforma de data warehouse na nuvem que oferece escalabilidade e desempenho.
    
    **Amazon S3**: O serviço de armazenamento de objetos da AWS, muito utilizado para carregar dados em bruto

A seguir encontra-se um exemplo de ETL e Pipeline de dados:

![Fundamentos em Engenharia de Dados - Página 1](https://github.com/user-attachments/assets/f730797f-9130-40db-a80e-851a0ab8c437)

Links úteis:

- Stitch: https://www.stitchdata.com/docs/integrations/
- AWS Glue: https://aws.amazon.com/pt/glue/
- Nifi: https://nifi.apache.org/
- Talend: https://www.talend.com/
- Pentaho: https://pentaho.com/products/pentaho-data-integration/
- Spark: https://spark.apache.org/
- Dataflow: https://cloud.google.com/dataflow?hl=pt-BR
- Kafka Streams: https://kafka.apache.org/documentation/streams/
- Airflow: https://airflow.apache.org/
- AWS Redshift: https://aws.amazon.com/pt/redshift/
- BigQuery: https://cloud.google.com/bigquery
- Azure Synapse Analytics: https://azure.microsoft.com/pt-br/products/synapse-analytics
- Snowflake: https://www.snowflake.com/pt_br/
- AWS S3: https://aws.amazon.com/pt/s3/
