import os

# Define the base directory
base_dir = "/Users/dimasjackson/blog/docs"

# Ensure the base directory exists
os.makedirs(base_dir, exist_ok=True)

# Creating the requested Markdown files with content
file_paths = [
    os.path.join(base_dir, "projetos.md"),
    os.path.join(base_dir, "publicacoes.md"),
    os.path.join(base_dir, "certificacoes.md"),
    os.path.join(base_dir, "resenhas_livros.md"),
    os.path.join(base_dir, "contato.md")
]

# Content templates for each file
contents = {
    "projetos.md": """\
# Projetos

## Meus Projetos

Aqui estão alguns dos projetos em que trabalhei:

- **Projeto 1**: [Descrição breve ou link.]
- **Projeto 2**: [Descrição breve ou link.]

Explore mais detalhes sobre cada projeto acima!
""",
    "publicacoes.md": """\
# Publicações

## Minhas Publicações Acadêmicas e Técnicas

- **Artigo 1**: [Título do Artigo] - Publicado em [Evento/Revista].
- **Artigo 2**: [Título do Artigo] - Publicado em [Evento/Revista].

Fique à vontade para acessar os links para mais detalhes.
""",
    "certificacoes.md": """\
# Certificações

## Certificações Obtidas

- **Certificação 1**: [Descrição, instituição emissora.]
- **Certificação 2**: [Descrição, instituição emissora.]

Estes certificados refletem minha jornada de aprendizado contínuo.
""",
    "resenhas_livros.md": """\
# Resenhas de Livros

## Livros que me inspiraram

- **Livro 1**: [Título do Livro] - Minha resenha ou opinião.
- **Livro 2**: [Título do Livro] - Minha resenha ou opinião.

Leia as resenhas completas para se inspirar também!
""",
    "contato.md": """\
# Contato

## Fale Comigo

Preencha o formulário abaixo ou use as redes sociais para entrar em contato:

- **Email**: seu-email@dominio.com
- **LinkedIn**: [Seu Perfil](#)
- **GitHub**: [Seu Perfil](#)
- **Twitter**: [Seu Perfil](#)

Aguardo ansiosamente para ouvir de você!
"""
}

# Creating files with their respective content
for path in file_paths:
    file_name = path.split("/")[-1]
    with open(path, "w") as file:
        file.write(contents[file_name])

"Arquivos criados com sucesso."
