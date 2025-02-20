listeMessages = \
{
    "ERR_001" : "",
    "token_refresh_401" : "Erreur de token",
    "no_data_found" : "Donnees non disponible",
    "client_not_found": "Client inconnu",
    "Invalid_request": "Erreur requete",
    "Internal Server error": "Erreur Interne Enedis",
    "result_500": "Erreur interne Enedis(500)",
    "UNKERROR_001": "Erreur interne Enedis(001)",
    "UNKERROR_002": "Erreur timeout",
}

def getMessage( codeMessage ):
    if ( codeMessage in listeMessages.keys()):
        return listeMessages[ codeMessage ]
    else:
        return codeMessage