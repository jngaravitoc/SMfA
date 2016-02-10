#This function generate N random number 'eps_i' between 0.1 and 5.0, the
#function generate a second random number 'decisition' between 0 and
#1. if decistion <= f(eps_i) the photon is taking into account.
def rejectionn(N):
    edf = np.ones(N)*10
    for i in range(N):
        eps_i = np.random.random() * 5.0
        decisition = np.random.random()
        if decisition <= BBDF(eps_i, norm):
            edf[i] = eps_i
    index = np.where(edf!=10)[0]
    return edf[index]
