
def organize_text(text):
    text = text.replace('\n', ' ').replace(',', '').replace('.', '').replace('  ', ' ').lower().strip().split(' ')

    return text

def organize_parameters(organized_text):
    parameters = []
    for id, l in enumerate(organized_text):
        pos_l = id
        parameters_unic = []
        for c in range(1, len(organized_text)):
            if pos_l+c < len(organized_text):
                parameters_unic.append([l, organized_text[pos_l+c]])
            if pos_l-c > -1:
                parameters_unic.append([l, organized_text[pos_l-c]])
        parameters.append(parameters_unic)

    for id, p in enumerate(parameters):
        pos_p = id
        new_p = []
        for s in p:
            if not s in new_p and s[0] != s[1]:
                new_p.append(s)

        parameters[pos_p] = new_p

    return parameters

def join_same_parameters(organized_parameters, organized_text):
    text_set = set(organized_text)
    joined_same_parameters = []
    for w in text_set:
        w_par = []
        for p in organized_parameters:
            if p[0][0] == w:
                w_par.append(p)

        new_para = []
        for i in range(0, len(w_par[0])):
            for par in w_par:
                new_para.append(par[i])
        
        repetitoff_new_para = []
        for n in new_para:
            if not n in repetitoff_new_para:
                repetitoff_new_para.append(n)

        joined_same_parameters.append(repetitoff_new_para)
    
    return joined_same_parameters

def parameters_words_text(text):
    organized_text = organize_text(text)
    #print(organized_text)
    organized_parameters = organize_parameters(organized_text)
    #print(organized_parameters)
    joined_same_parameters = join_same_parameters(organized_parameters,organized_text)

    return joined_same_parameters

text = """A amizade consegue ser tão complexa.
Deixa uns desanimados, outros bem felizes.
É a alimentação dos fracos
É o reino dos fortes.

Faz-nos cometer erros
Os fracos deixam se ir abaixo
Os fortes erguem sempre a cabeça
Os assim assumem-nos.

Sem pensar conquistamos
o mundo geral
e construímos o nosso pequeno lugar,
deixando brilhar cada estrelinha.

Estrelinhas
Doces, sensíveis, frias, ternurentas.
Mas sempre presentes em qualquer parte.
Os donos da amizade."""

parameters = parameters_words_text(text)

