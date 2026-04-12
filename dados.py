gene_list = [
    "epsilon-adaptin",
    "PIK3CA",
    "GAPDH",
    "TcUGD",
    "TcGP72"
]

lista_gene_epsilon_adaptin = [
    len(gene_list[0]),
    (gene_list[0])[0:2],
    gene_list[0].count("a"),
    "hu" in gene_list[0],
]


lista_gene_PIK3CA = [
    len(gene_list[1]),
    (gene_list[1])[0:2],
    gene_list[1].count("a"),
    "hu" in gene_list[1],
]


lista_gene_GAPDH = [
    len(gene_list[2]),
    (gene_list[2])[0:2],
    gene_list[2].count("a"),
    "hu" in gene_list[2],
]


lista_TcUGD = [
    len(gene_list[3]),
    (gene_list[3])[0:2],
    gene_list[3].count("a"),
    "hu" in gene_list[3],
]


lista_gene_TcGP72 = [
    len(gene_list[4]),
    (gene_list[4])[0:2],
    gene_list[4].count("a"),
    "hu" in gene_list[4],
]


gene_list_dict = {
    gene_list[0] : lista_gene_epsilon_adaptin,
    gene_list[1] : lista_gene_PIK3CA,
    gene_list[2] : lista_gene_GAPDH,
    gene_list[3] : lista_TcUGD,
    gene_list[4] : lista_gene_TcGP72



}
