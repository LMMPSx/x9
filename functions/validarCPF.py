def validarCPF(cpf):
    if cpf == '-':
        return cpf
    elif len(cpf) < 11:
        return f'0{cpf}'
    else:
        return cpf
