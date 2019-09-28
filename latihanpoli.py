class FakultasTeknik(object):
    def __init__(self, univ, fak, ta):
        self.universitas = univ
        self.fakultas = fak
        self.tahunAjar = ta

    def cetakData(self):
        print("Universitas\t: ", self.universitas)
        print("Fakultas\t: ", self.fakultas)
        print("Tahun Ajar\t: ", self.tahunAjar)

class TeknikKomputer(FakultasTeknik):
    def __init__(self, univ, fak, ta, jmlang):
        self.universitas = univ
        self.fakultas = fak
        self.tahunAjar = ta
        self.jumlahAngkatan = jmlang
    def cetakData(self):
        print("Universitas\t: ", self.universitas)
        print("Fakultas\t: ", self.fakultas)
        print("Tahun Ajar\t: ", self.tahunAjar)
        print("Jumlah Angkatan\t: ", self.jumlahAngkatan)

class VokasionalMekatronika(FakultasTeknik):
    def __init__(self, univ, fak, ta, jmlang):
        self.universitas = univ
        self.fakultas = fak
        self.tahunAjar = ta
        self.jumlahAngkatan = jmlang
    def cetakData(self):
        print("Universitas\t: ", self.universitas)
        print("Fakultas\t: ", self.fakultas)
        print("Tahun Ajar\t: ", self.tahunAjar)
        print("Jumlah Angkatan\t: ", self.jumlahAngkatan)

class PTIK(FakultasTeknik):
    def __init__(self, univ, fak, ta, jmlang, jur):
        self.universitas = univ
        self.fakultas = fak
        self.tahunAjar = ta
        self.jumlahAngkatan = jmlang
        self.jurusan = jur
    def cetakData(self):
        print("Universitas\t: ", self.universitas)
        print("Fakultas\t: ", self.fakultas)
        print("Tahun Ajar\t: ", self.tahunAjar)
        print("Jumlah Angkatan\t: ", self.jumlahAngkatan)
        print("Jurusan\t: ", self.jurusan)

def main():
    obj = FakultasTeknik('Universitas Negeri Makassar', 'Teknik', 2019)
    print("KELAS INDUK")
    obj.cetakData()

    del obj

    obj = TeknikKomputer('Universitas Negeri Makassar', 'Teknik', 2019, 2)
    print("\nTEKNIK KOMPUTER")
    obj.cetakData()

    del obj

    obj = VokasionalMekatronika('Universitas Negeri Makassar', 'Teknik', 2019, 2)
    print("\nVOKASIONAL MEKATRONIKA")
    obj.cetakData()

    del obj

    obj = PTIK('Universitas Negeri Makassar', 'Teknik', 2019, 10, "Pendidikan Teknik Elektro")
    print("\nPTIK")
    obj.cetakData()

if __name__ == "__main__":
    main()