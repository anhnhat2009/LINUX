class SinhVien:
	MSSV = "001"
	HoTen = "Mai A"
	Khoa = "57"
	def __init__(self,MSSV,HoTen,Khoa):
		self.MSSV = MSSV
		self.HoTen = HoTen
		self.Khoa = Khoa
	def setMSSV(self,MSSV):
		self.MSSV = MSSV
	def getMSSV(self):
		return self.MSSV
	def setHoTen(self,HoTen):
		self.HoTen = HoTen
	def getHoTen(self):
		return self.HoTen
	def setKhoa(self,Khoa):
		self.Khoa = Khoa
	def getKhoa(self):
		return self.Khoa
    

