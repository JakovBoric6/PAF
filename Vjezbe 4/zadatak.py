#Napišite program koji crta putanju nabijene čestice u konstantnom električnom i magnetnom polju. Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom magnetnom polju B⃗ = (0, 0, B)
#i ima sve tri komponente početne brzine različite od 0. Kako se u tom slučaju giba elektron, a kako pozitron?
#Prikažite grafove gibanja elektrona i pozitrona za nekoliko kombinacija vrijednosti električnog i magnetskog
#polja.



import numpy as np
import matplotlib.pyplot as plt

def simuliraj_gibanje(q,m,E,B,v0,t_max,dt):
    
    t=np.arange(0,t_max,dt)
    n=len(t)
    
    #predložio AI- cini mi se jako pametno zapravo dobijamo mjesta za pohraniti x,y,z koordinate sto je vidljivo po 3 stupca ali takoder  i imamo n redova za svaki dt koji je potreban, nazalost ovaj pristup je takoder zahtjevao moju najvecu korist AI-a i ostalih alata do sada na ovom kolegiju jer bi uvijek nastala neka greška koju sam ne bih mogao pronaci, bilo to stavljanje jedne 0 umijesto 3 ili definiraanje za i a ne i+1 kako bi dobili novu azuriranu dok jos uvijek imamo pohranjenu staru
    r = np.zeros((n,3))
    v = np.zeros((n,3))
    
    #zbog moj prijasnjeg pristupa moram navoditi o kojem polozaju u tablici ja zelim pristupiti
    r[0] =[0,0,0]
    v[0] =v0
    
    #sad cu rjesit numericki pomocu Eulerove metode i sad mi je jako bitno naglasiti da moram ici do n-1 jer sam definirao i+1 
    for i in range(n-1):
        #za Lorentzovu: F=q*(E+vxB)
        sila =q*(np.array(E)+np.cross(v[i],B))
        
        
        a=sila/m


        v[i+1]=v[i]+a*dt
        r[i+1]=r[i]+v[i]*dt
        
    return r


m=1.0
naboj_p=1.0
naboj_e=-1.0
p_v =[1.0,0.5,0.2] 
B_p =[0,0,1.0]         
korak=0.01                   
t=50                  

#sada imamo prvi slucaj kad je E=0
E_nula=[0,0,0]
putanja_e_B = simuliraj_gibanje(naboj_e, m, E_nula, B_p, p_v, t, korak)
putanja_p_B = simuliraj_gibanje(naboj_p, m, E_nula, B_p, p_v, t, korak)

#sada za drugi slucaj imamo kombinaciju B i E
E_p=[0.1,0,0] #dodao sam neko polje u x smjeru
putanja_e_EB=simuliraj_gibanje(naboj_e, m, E_p, B_p, p_v, t, korak)
putanja_p_EB=simuliraj_gibanje(naboj_p, m, E_p, B_p, p_v, t, korak)





fig =plt.figure(figsize=(14, 6))

# graf 1, samo magnetsko polje
ax1 =fig.add_subplot(121,projection="3d") #ovo 121 sam naucio na https://www.geeksforgeeks.org/ prva jedinica je za red onda je 2 za broj stupaca a zadnja 1 nam kaze da je to prvi graf u plotu
ax1.plot(putanja_e_B[:,0], putanja_e_B[:,1], putanja_e_B[:,2],label="elektron(E=0)",color="blue")
ax1.plot(putanja_p_B[:,0], putanja_p_B[:,1], putanja_p_B[:,2],label="pozitron(E=0)",color="red")
ax1.set_title("gibanje u konst_B polju")
ax1.set_xlabel("x"); ax1.set_ylabel("y"); ax1.set_zlabel("z")
ax1.legend()

# graf 2, za magnetsko i elektricno
ax2 =fig.add_subplot(122,projection="3d")
ax2.plot(putanja_e_EB[:,0], putanja_e_EB[:,1], putanja_e_EB[:,2],label="elektron(E+B)",color="cyan")
ax2.plot(putanja_p_EB[:,0], putanja_p_EB[:,1], putanja_p_EB[:,2],label="pozitron(E+B)",color="orange")
ax2.set_title("gibanje u E i B polju")
ax2.set_xlabel("x"); ax2.set_ylabel("y"); ax2.set_zlabel("z")
ax2.legend()

plt.tight_layout()
plt.show()

