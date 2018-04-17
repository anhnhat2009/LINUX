from HDT import SinhVien
S=[]
S.append(SinhVien("001","Mai A","57"))
S.append(SinhVien("002","Tran B","57"))
S.append(SinhVien("003","Le C","57"))
S.append(SinhVien("004","Pham Q","57"))
S.append(SinhVien("005","Ngo M","57"))
    
for i in range(0,len(S)):
	print(S[i].HoTen,S[i].MSSV,S[i].Khoa)

