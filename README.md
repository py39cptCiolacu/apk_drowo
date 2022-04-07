## Aplicatie Drowo

** cod cu cat mai mult comentariu, si cu nume de variabile cat mai intuitive <br>
** de fiecare data cand modifici README-ul, 'Vx, backend/frontend' cum e descris si la pct 1 

1. Comenzi git : https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html
   - in principiu vei folosi in ordinea asta: git add . , git commit - m , git push
   - de fiecare daca cand dai git commmit -m, mesajul sa fie 'Vx, backend/frontend', unde x e nr versiunii la care am ajuns, si backend/frontend partea unde ai facut modicari; dupa care vii aici la 3. Versiuni si dai detalii
 
2. Paginile din aplicatie:
   - home -> cuprinde meniu, descriere eveniment, countdown
   - login_team -> pentru logarea echipelor
   - team -> descrierea fiecarei echipe, numele participantilor (customizabil de catre ei), punctele obtinute si mai vedem
   - admin -> controlul nostru cat mai simplu asupra aplicatiei
   - shop -> de stabilit exact

3. Versiuni:
  - V1- backend :  - am creat baza aplicatiei: paginile home, login_team, team, admin.
                   - am creat baza de date ce curprinde: username, password (per echipa pentru logare), puncte (nume de variabila ce trebuie pus in engleza ca sa ramanem cu toate asa), names (voi face ca fiecare echipa sa iti puna ea numele participantilor si sa apara pe pagina team)
                   - am creat base.html -> asta e baza tuturor html-urilor pe care le vom avea. Va cuprinde doar chestiile comune pentru toate.
