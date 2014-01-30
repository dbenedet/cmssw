import FWCore.ParameterSet.Config as cms

fileNames= cms.untracked.vstring(
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/0829F19F-846A-E311-94B2-0025905A6082.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/0E9E2546-846A-E311-9D3D-003048678FB4.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/0EB55E61-826A-E311-ADEC-0025905938A4.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/10B750A5-846A-E311-9592-0025905A608E.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/123ED641-846A-E311-93BE-002618943959.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/123ED9B3-826A-E311-AF12-002618FDA216.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/2C06CF6A-856A-E311-A836-003048678B26.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/2E3C896C-826A-E311-82B3-0025905A60B6.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/305829D8-856A-E311-AFE8-0026189438C0.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/3429D1AE-826A-E311-A9B8-002354EF3BDD.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/34CB4F4B-846A-E311-B88D-0026189438E4.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/444BF5BC-876A-E311-BAEE-0026189438DE.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/44E2E29A-846A-E311-8AE4-003048678BAE.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/485991CD-826A-E311-AE99-003048FFD75C.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/488F0464-846A-E311-81A5-0025905A6138.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/56CFEE9E-846A-E311-954D-0025905964B4.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/56E883B1-826A-E311-B4A0-002618943865.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/5C9DF5A5-846A-E311-AF51-002590596498.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/62373780-876A-E311-B8E0-0025905A608E.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/70A4DFF0-986A-E311-AB3E-0025905A6110.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/7C08D8AD-826A-E311-BD2F-00261894384A.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/7E21EBB1-826A-E311-BD05-00261894390E.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/7EB332B0-826A-E311-9754-0026189438C0.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/8A4C6C79-856A-E311-A62C-00259059642A.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/8E29553D-846A-E311-9B17-00304867908C.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/926EE768-826A-E311-87E3-003048FFCB6A.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/9664C3C9-826A-E311-810D-0025905A6076.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/9A631794-846A-E311-95D7-0025905A609E.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/9C1EE369-856A-E311-AE78-00248C65A3EC.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/9E81C769-826A-E311-809D-0025905A607A.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/A0CA4CB7-826A-E311-AE3F-0026189438C4.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/A4AF6F90-846A-E311-9768-002618943986.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/A4B32CB3-826A-E311-911E-0026189438C2.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/A4B7629A-846A-E311-A04B-0025905A6122.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/A868206B-826A-E311-B0DF-0025905A613C.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/B253FAE7-8B6A-E311-8633-0025905A6076.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/B47A6EB3-826A-E311-B9AD-002618943951.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/BE364D50-826A-E311-82DB-003048679188.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/BE856EB7-826A-E311-824A-0026189438C4.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/C0B733B4-826A-E311-B814-002618943967.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/D09C0ECB-826A-E311-A920-0025905964B6.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/D0D4D68B-856A-E311-805D-003048678AE2.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/D2C62B2C-886A-E311-A76D-0025905A6132.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/D4E501BC-A66A-E311-9E11-003048D42D92.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/D66C5E6B-856A-E311-900A-0026189438E4.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/E0C5CCD3-826A-E311-AC17-0025905964BA.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/EC82226F-826A-E311-B803-0025905938A8.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/EE5472BE-826A-E311-9FA3-002354EF3BE6.root',
    '/store/relval/CMSSW_7_0_0_pre11/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/POSTLS162_V4-v1/00000/F0127B3E-8A6A-E311-9A07-002590593902.root'
     )

