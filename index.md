## About Me 🧔🏻‍♂️
<img src="https://github.com/dimasjackson/dimasjackson.github.io/assets/114688989/e0d362d5-8bb9-49ba-8f0d-f5cb0e0d94f5" width="150" />

<div style="text-align: justify"> 

Hello! I am starting a new journey in AI systems design at the greatest bank of the Euro Zone (2021), Santander!

I worked to improve data quality/governance at one of the largest private universities in Brazil, @Mackenzie, my expertise is in the design of robust Data Extraction, Transformation and Loading pipelines, strategic application of generative AI (using Langchain, ReAct Agents , embeddings) and building a semantic Data Lake, using Knowledge Graphs and RDFS/OWL.

Additionally, my skills include programming in Python and the efficient low code analysis tool KNIME Analytics. I have experience in Machine Learning and creating interactive dashboards in Power BI, transforming raw data into actionable insights.

I developed a robust ecosystem in the AWS cloud of PL/SQL procedures and functions, specifically designed to process non-relational data from APIs, optimizing data loads by up to 400%.

![Static Badge](https://img.shields.io/badge/Python-advanced-green?logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/PL%2FSQL-advanced-green?logo=postgresql&logoColor=white)
![Static Badge](https://img.shields.io/badge/Power%20BI-advanced-green?logo=powerbi&logoColor=white)
![Static Badge](https://img.shields.io/badge/Knime-advanced-green?logo=alchemy&logoColor=white)
![Static Badge](https://img.shields.io/badge/Wikibase-advanced-green?logo=wikidata&logoColor=white)
![Static Badge](https://img.shields.io/badge/SPARQL-advanced-green?logo=graphql&logoColor=white)

![Static Badge](https://img.shields.io/badge/Scikit--learn-intermediate-yellow?logo=scikitlearn&logoColor=white)
![Static Badge](https://img.shields.io/badge/Git-intermediate-yellow?logo=git&logoColor=white)
![Static Badge](https://img.shields.io/badge/Linux-intermediate-yellow?logo=linux&logoColor=white)
![Static Badge](https://img.shields.io/badge/Docker-intermediate-yellow?logo=docker&logoColor=white)
![Static Badge](https://img.shields.io/badge/Bash-intermediate-yellow?logo=gnubash&logoColor=white)
![Static Badge](https://img.shields.io/badge/Cloud-intermediate-yellow?logo=googlecloud&logoColor=white)

## Projects 📊

### Knowledge Graph Implementation
<center>
<img src="https://github.com/dimasjackson/dimasjackson.github.io/assets/114688989/a7f89de3-2b20-4434-ad6f-56cea0ce11f2" width="400" /> 
</center>

**Situation:** In response to the growing complexity of data integration and knowledge management within the organization, there arose a need for a scalable and interoperable solution to facilitate data discovery, integration, and sharing across disparate systems and domains.

**Task:** The task at hand was to design and implement a knowledge graph infrastructure capable of consolidating heterogeneous data sources, enriching data semantics through ontology modeling, and enabling intuitive query capabilities for users across the organization.

**Action:** The project team adopted Protegé as the primary tool for ontology modeling, allowing for the formal representation of domain knowledge and relationships. Wikibase, integrated with MediaWiki, was chosen as the collaborative platform for capturing and curating knowledge artifacts. Open Refine was utilized for data cleaning and preprocessing, ensuring data quality and consistency within the knowledge graph. Furthermore, SPARQL queries were employed to extract insights and perform complex analytics on the knowledge graph. All the components where deployed in Docker containers being highly scalable.

**Result:** Through the successful execution of a proof of concept followed by a four-month pilot phase, the knowledge graph implementation demonstrated its efficacy in enabling seamless data integration, enhancing discoverability, and promoting knowledge sharing across the organization. The project is now poised for production deployment, offering a scalable and robust solution for addressing the organization's evolving data management needs.

#### Tools
![Static Badge](https://img.shields.io/badge/Protege-RDF-green)
![Static Badge](https://img.shields.io/badge/BlazeGraph-SPARQL-green)
![Static Badge](https://img.shields.io/badge/MediaWiki-html-green)
![Static Badge](https://img.shields.io/badge/Wikibase-php-green)
![Static Badge](https://img.shields.io/badge/Docker-yml-green)

### Enterprise Service Bus Functions and Procedures
<center>
<img src="https://github.com/dimasjackson/dimasjackson.github.io/assets/114688989/ff4d16c9-f077-4f90-a31b-f7171ed47bbf" width="400" /> 
</center>

**Situation:** With the implemententation of the new ERP, the company identified the necessity for integration of hundreds of legacy system and the construction of a Enterprise Service Bus - ESB, to remove data silos. 

**Task:** The data coming from ESB APIs had to be processed and storage with efficiency, being transformed from JSON documents into a structured database, to allow retrieval and  near real time update.

**Action:** Our team designed and built an ecosystem of procedures and functions in PL/SQL for processing non-relational data coming from APIs and storing it in the relational database in AWS cloud serverless database (Amazon RDS), combining the best features of both paradigms.

**Result:** This project allowed the company data to be processed and updated much faster and with better reliability. The functions and procedures increased the performance by up to 400% across data loads and reduced the cost to retrieve data. Improving the processing and storage we achieved faster data delivery for analytics and BI. Also, a better data quality was reached, since the data was standardized and integrated, allowing more confident data driven decisions. 

#### Tools
![Static Badge](https://img.shields.io/badge/Postgres-SQL-green)
![Static Badge](https://img.shields.io/badge/SQL%20Server-SQL-green)
![Static Badge](https://img.shields.io/badge/AWS-Cloud-green)
![Static Badge](https://img.shields.io/badge/PgSQL-PL-green)

### Gen AI Chat to Enterprise Data 
<center>
<img src="https://github.com/dimasjackson/dimasjackson.github.io/assets/114688989/044daa6e-17dc-4679-b997-3581998febf1" width="400" />
</center>

**Situation:**  The need arises to enhance user interaction by enabling natural language questions and answers within the Wikibase platform. This will facilitate a more user-friendly and intuitive experience for accessing information stored in the Enterprise Knowledge Graph.

**Task:** Create a Wikibase LangChain agent, an intelligent natural language processing system, that can understand and respond to user queries in a conversational manner. The goal is to improve the accessibility of information stored in the private Wikibase instance, making it easier for users to retrieve relevant data through natural language interactions.

**Action:** I conducted a thorough analysis of existing natural language processing (NLP) technologies and solutions and evaluate potential tools and frameworks suitable for integrating NLP capabilities into the Wikibase environment. Now I am implementing the necessary NLP components using state-of-the-art algorithms and models, and integrating the LangChain agent with the private Wikibase instance, ensuring compatibility and security measures are in place.
  
**Result:** The Wikibase LangChain agent have been deployed in the private Wikibase instance, enabling users to interact with the system using natural language queries. This will result in a more user-friendly and accessible environment, enhancing the overall user experience within the organization. The stakeholders will be able to ask questions in a conversational manner and receive relevant information from the Wikibase instance, fostering increased efficiency and engagement with the data stored in the Knowledge Graph without the necessity of learning SPARQL language or call analysts to answer simple business questions. 

#### Tools
![Static Badge](https://img.shields.io/badge/LangChain-Python-green)
![Static Badge](https://img.shields.io/badge/Google%20Gemini-LLM-green)
![Static Badge](https://img.shields.io/badge/Ollama-AI-green)
![Static Badge](https://img.shields.io/badge/Wikibase-SPARQL-green)

### Data Extraction, Transforming and Load (ETL) Pipelines
<center>
<img src="https://github.com/dimasjackson/dimasjackson.github.io/assets/114688989/00df3dcc-4bab-4bbc-afa7-169835b65001" width="400" />
</center>

**Situation:** The company’s teams need data of better quality and compliance, delivered quickly and in a secure environment for analysis.

**Task:** We had to integrate different data sources into pipelines capable of cleaning, anonymizing, and loading data to third-party platforms.

**Action:** I designed and built several ETL pipelines, extracting data from various sources such as CRM system APIs, SQL databases, and the Enterprise Data Warehouse. I combined different SQL tools, including Microsoft SQL Server, PostgreSQL, and MySQL, with the versatile and low-code Knime Analytics Platform. The extracted data was cleaned, normalized, and loaded into a secure workspace for analytics and BI development within a Microsoft Power BI Workspace.

**Result:** This strategy significantly improved the efficiency of delivering high-quality data to different teams within the company. It also boosted confidence in the analyses conducted. Additionally, I contributed to standardizing the organization’s data delivery policies, thereby enhancing Data Governance and Compliance. 

#### Tools
![Static Badge](https://img.shields.io/badge/Postgres-SQL-green)
![Static Badge](https://img.shields.io/badge/SQL%20Server-SQL-green)
![Static Badge](https://img.shields.io/badge/KNIME-Low%20code-green)
![Static Badge](https://img.shields.io/badge/Jupyter%20Lab-Python-green)

## More Projects 🚀

* [Denominational School Analysis](projects/school.md)
* [Estimation of the Fraction of Matter and Energy of the Universe](projects/universe.md)
* [Space X Falcon 9 Landing Success Prediction](projects/spacex.md)
* [YouTube Channel Evolution During Pandemics](projects/youtube.md)

## Contact 📬

Feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/dimas-jackson) or contact by email [dimas.jackson.ds@gmail.com](mailto:dimas.jackson.ds@gmail.com). I'm always open to interesting discussions and collaborations!

Thanks for visiting!

