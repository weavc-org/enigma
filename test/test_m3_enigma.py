from ..enigma.m3.enigma import enigma
from ..enigma.m3.settings import settings

class TestEnigma:
    # invalid characters, rotors, reflectors, plugboard, ring settings, rotor settings, all together
    
    def test_encrypt_default_settings(self):
            s, e = enigma().encrypt('NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
            assert s == 'YUMJMZFVOTEPJPQDITFZLTARTGRUJAXLWLBDFQDXDLUYNQRMIOZNREBWTGQS'

    def test_decrypt_default_settings(self):
            s, e = enigma().encrypt('YUMJMZFVOTEPJPQDITFZLTARTGRUJAXLWLBDFQDXDLUYNQRMIOZNREBWTGQS')
            assert s == 'NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG'

    def test_encrypt_invalid_settings(self):
        sets = settings()
        sets.rotor_settings = [100,0,100]

        _, e = enigma(sets).encrypt('NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
        assert e is not None

    def test_encrypt_ring_settings(self):
        sets = settings()

        is_valid, _ = sets.set_values(left_ring_setting='H', middle_ring_setting='L', right_ring_setting='K')
        assert is_valid is True
        
        s, _ = enigma(sets).encrypt('NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
        assert s == 'YTWHPKBALVPHBOIKMYHUHZFULMUEYUIPZMSCZLHVPBBOFPUYFIVQBLOHTIUU'

        s, _ = enigma(sets).encrypt('YTWHPKBALVPHBOIKMYHUHZFULMUEYUIPZMSCZLHVPBBOFPUYFIVQBLOHTIUU')
        assert s == 'NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG'

    def test_encrypt_rotor_settings(self):
        sets = settings()

        is_valid, _ = sets.set_values(left_rotor_setting='H', middle_rotor_setting='L', right_rotor_setting='K')
        assert is_valid is True
        
        s, _ = enigma(sets).encrypt('NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
        assert s == 'GZBSEAXDRVMDDSQINJKJJQKKYIYDSJFGYMHCSVCUPLUYFAKBYMYEZDYYUXFM'

        s, _ = enigma(sets).encrypt('GZBSEAXDRVMDDSQINJKJJQKKYIYDSJFGYMHCSVCUPLUYFAKBYMYEZDYYUXFM')
        assert s == 'NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG'

    def test_encrypt_plugboard(self):
        sets = settings()

        is_valid, _ = sets.set_values(plugboard='az,lk,ui,er,jy,wf')
        assert is_valid is True
        
        s, _ = enigma(sets).encrypt('NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
        assert s == 'JIBGMAWVODRPYPVDGGPAKTZEGGEHYZXXMVBDZIDXVKIJGVEAUDZNIRWFNHQS'

        s, _ = enigma(sets).encrypt('JIBGMAWVODRPYPVDGGPAKTZEGGEHYZXXMVBDZIDXVKIJGVEAUDZNIRWFNHQS')
        assert s == 'NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG'

    def test_encrypt_plugboard(self):
        sets = settings()

        is_valid, _ = sets.set_values(reflector='C')
        assert is_valid is True
        
        s, _ = enigma(sets).encrypt('NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
        assert s == 'ZGWGWYKJXSZIQFJREBGJMIKUOPEBUVUKRFJOMIPSLPPEUZXILWAIEUXJOMZI'

        s, _ = enigma(sets).encrypt('ZGWGWYKJXSZIQFJREBGJMIKUOPEBUVUKRFJOMIPSLPPEUZXILWAIEUXJOMZI')
        assert s == 'NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG'

    def test_invalid_characters(self):
        sets = settings()
        
        # shouldn't do anything with non A-Za-z characters at the moment 
        s, _ = enigma(sets).encrypt('NV KZ_HG,DH-MA(NG)SV2KS4YIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
        assert s == 'YU MJ_MZ,FV-OT(EP)JP2QD4ITFZLTARTGRUJAXLWLBDFQDXDLUYNQRMIOZNREBWTGQS'

        s, _ = enigma(sets).encrypt('YU MJ_MZ,FV-OT(EP)JP2QD4ITFZLTARTGRUJAXLWLBDFQDXDLUYNQRMIOZNREBWTGQS')
        assert s == 'NV KZ_HG,DH-MA(NG)SV2KS4YIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG'

    def test_rotors(self):
        sets = settings()
    
        is_valid, _ = sets.set_values(left_rotor='VI', middle_rotor='III', right_rotor='VIII')
        assert is_valid is True

        s, _ = enigma(sets).encrypt('NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
        assert s == 'GXTQYEIXXNTXJMBBMSVADVYWRFXKXCJFOXLCZWYSUVGXIBCXSSKXGQKRLXUR'

        s, _ = enigma(sets).encrypt('GXTQYEIXXNTXJMBBMSVADVYWRFXKXCJFOXLCZWYSUVGXIBCXSSKXGQKRLXUR')
        assert s == 'NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG'

    def test_all_togther(self):
        sets = settings()
        
        is_valid, _ = sets.set_values(left_rotor='VI', middle_rotor='III', right_rotor='VIII', 
                                    left_rotor_setting='H', middle_rotor_setting='L', right_rotor_setting='K',
                                    left_ring_setting='H', middle_ring_setting='L', right_ring_setting='K',
                                    plugboard='az,lk,ui,er,jy,wf', reflector='C')
        assert is_valid is True

        s, _ = enigma(sets).encrypt('NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
        assert s == 'VINNJLUZTQXKPQLTHLUANQVLJPANKRDLJTVHEVNRKIDYVSCHXISNTAJNACMO'

        s, _ = enigma(sets).encrypt('NVKZHGDHMANGSVKSYIZNOXQGKNSZOXBUIWOQUEOCIHVVKLGKGAEMKXLPWLVG')
        assert s == 'VINNJLUZTQXKPQLTHLUANQVLJPANKRDLJTVHEVNRKIDYVSCHXISNTAJNACMO'

        
        