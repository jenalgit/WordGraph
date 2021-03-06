from word.grapher import WordGrapher, StopwordsTokenizer
import unittest


class GrapherTest(unittest.TestCase):

    doc = """museumnya bagus.., kalo lagi liburan rame banget, ga cuma wisatawan dari Indonesia, tapi dari luar
    negeri juga... luas banget lagi di dalemnya.... seru..!! hehehehe"""
    docs = [
        """Museum jakarta, banyak peninggalan Zaman dulu, trus barang2nya udah Tua dan rapuh.. banyak cerita d museum ini
        tentang kota jakarta..di museum ini seringkali foto-foto karena tempatnya bersejarah bgt jadi harus di
        abadikan. Kayaknya museum sejarah jakarta menjadi spot 'penting' belakangan ini. tiap weekend pasti PENUH sama
        orang-orang yang mau foto-foto. gue sampe sempet ngantri cuma buat foto gedung doang.""",

        """mau weekend tanpa mesti ngabisin duit ya dateng aja ke sini... kalo yang hobi fotografi juga banyak spot2 yang
        menarik untuk difoto disini... kalo pengen moto arsitekturnya disarankan dateng pagi2 buta soalnya kalo udah agak
        siangan pasti bakalan rame banget""",

        """ini dia yang jarang dilakukan anak muda, habis hang out bareng teman2 langsung cabut ke mall atau main ke rumah
        teman. cobain sensasi berbeda dengan datang ke museum apalagi sebentar lagi ada konser avril. pasti seru banget
        ngajakin si doi idola kita main ke situ, supaya lebih tau juga gimana sejarah kota yang tempati untuk konser
        itu. :)""",

        """weekend seru juga kalau berkunjung ke museum sejarah jakarta, selain karena di halamannya biasanya ramai
        orang-orang dan kita bisa hunting foto, di museum ini juga kalau weekend ada pertunjukkan mystery of batavia..
        tambah asyik deh kalau jalan-jalan ke sini :)""",

        """Terletak di kawasan kota tua tepatnya dengan luas lebih dari 1.300 meter persegi. Dahulu gedung ini merupakan
        balai kota lalu diresmikan menjadi Museum Fatahillah pada 30 Maret 1974. Kita dapat menemui berbagai objek di
        museum ini seperti perjalanan sejarah Jakarta, replika peninggalan masa Tarumanegara dan Pajajaran, hasil
        penggalian arkeologi, koleksi tentang kebudayaan Betawi, numismatic, dan becak. Ada juga patung Dewa Hermes dan
        meriam Si Jagur yang dianggap mempunyai kekuatan magis serta bekas penjara bawah tanah yang dulu sempat digunakan
        pada zaman penjajahan Belanda. Benar-benar museum yang patut dikunjungi, kita bisa hunting foto ataupun sekedar
        menambah pengetahuan, apalagi dengan arsitekturnya yang klasik bergaya Belanda, akan menciptakan aura yang berbeda
        ketika kita masuk ke dalamnya.""",

        """Merupakan aset bersejarah kebanggan Jakarta. Berada di komplek Kota Tua yang terkenal indah banget, museum ini
        juga jadi salah satu daya tarik banyak pengunjung, ngga cuma lokal tapi juga mancanegara. Pas masuk ke dalamnya,
        atmosfernya langsung beda karena gaya arsitektur Belanda yang masih dipertahankan. Kalau mau keliling bisa
        ditemenin sama guide ataupun bisa juga sendiri. Mau wisata pendidikan sejarah Jakarta sekaligus hunting foto
        semuanya lengkap di sini. :)""",

        """Weekend pagi seru juga datang kesini bisa hunting foto2 yang keren dari tempat ini. Arsitektur bangunan disini
        unik2 dan super jadul seru rasanya kesini sekali2 for a change from the bustling city view that we have every
        day.""",

        """Dikawasan ini sering sekali dijadikan tempat untuk hunting foto modeling maupun prewedding. Hal tersebut
        dikarenakan setting tempat yang kuno dan klasik dan bernuansa jaman kolonial. Di tempat ini ada beberapa museum
        seperti museum fatahilah yang menceritakan sejarah jakarta dan museum wayang yang memamerkan semua koleksi wayang
        yang terdapat di Indonesia. Di Hall atau lapangan bagian tengah dari kawasan ini selalu ramai dikunjungi oleh
        masyarakat yang ingin bersantai dengan menyewa sepeda tua yang dapat digunakan untuk berkeliling dengan tarif
        perjam sebesar 20ribu saja. Jika kita lapar maka ada cafe Batavia yang selalu ramai dikunjungi. Kawasan kota tua
        ini juga sering dijadikan salah satu tempat yang wajib dikunjungi oleh orang asing yang sedang berkunjung ke
        jakarta jadi tidak heran terdapat banyak sekali bule yang berlalu-lalang disini. Bagian yang menjadi favorit gwa
        adalah saat malam hari terdapat wisata malam yang memanjakan mata. Di depan museum Fatahillah sering dibuat
        pertunjukan laser yang sangat indah dengan lampu-lampu sorot yang menawan. :)"""
    ]

    wg = None

    def setUp(self):
        self.wg = WordGrapher(doc=self.doc, docs=self.docs)

    def test_wordgraph_is_not_none(self):
        self.assertIsInstance(self.wg, WordGrapher, msg="WordGrapher object must be an instance of WordGrapher")
        self.assertIsNotNone(self.wg, msg="WordGrapher object is None")

    def test_wordgraph_tfidf(self):
        result = self.wg.analyze()

        self.assertIsNotNone(result, msg="TF-IDF Result must not be None")
        self.assertIsInstance(result, list, msg="TF-IDF Result must be a List instance")

    def test_wordgraph_graph(self):
        self.wg.analyze(count=1000, percentage=True)
        graph = self.wg.graph(word="banget")

        self.assertIsNotNone(graph, msg="Returned Graph object is None")
        self.assertIsInstance(graph, dict, msg="Returned Graph object must be a Dictionary")
        self.assertIsNotNone(graph['twos'], msg="Return Graph TWOS is None")
        self.assertIsNotNone(graph['tris'], msg="Return Graph TRIS is None")