from klass2 import *
kasutaja1 = Kasutaja("Timmu","Õunapuu")
kasutaja2 = Kasutaja("Oliver","Mõttus")
kasutaja3 = Kasutaja("Joonatan","Kelder")
kasutaja1.set_privileeg("root")
kasutaja2.set_privileeg("user")
kasutaja3.set_privileeg("user")
kasutaja1.set_domain("Domeen")
kasutaja2.set_domain("Domeen 2.0")
kasutaja3.set_domain("WorkGroup 3.0")


kasutaja1.kirjelda_kasutajat(kasutaja1.get_domain(),kasutaja1.get_privileeg())
kasutaja2.kirjelda_kasutajat(kasutaja2.get_domain(),kasutaja2.get_privileeg())
kasutaja3.kirjelda_kasutajat(kasutaja3.get_domain(),kasutaja3.get_privileeg())