import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("FWCore.Framework.test.cmsExceptionsFatal_cff")

# The following two lines reduce the clutter of repeated printouts
# of the same exception message.
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.destinations = ['cerr']
process.MessageLogger.statistics = []
process.MessageLogger.fwkJobReports = []

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(3)
)
process.source = cms.Source("EmptySource")

process.dsvsimple = cms.EDProducer("DSVProducer",
    size = cms.int32(8)
)

process.intdeque = cms.EDProducer("IntDequeProducer",
    count = cms.int32(12),
    ivalue = cms.int32(21)
)

process.intlist = cms.EDProducer("IntListProducer",
    count = cms.int32(4),
    ivalue = cms.int32(3)
)

process.intset = cms.EDProducer("IntSetProducer",
    start = cms.int32(100),
    stop = cms.int32(110)
)

process.intvec = cms.EDProducer("IntVectorProducer",
    count = cms.int32(9),
    ivalue = cms.int32(11)
)

process.intvecrefvec = cms.EDProducer("IntVecRefVectorProducer",
    target = cms.string('intvec')
)

process.intvecreftbvec = cms.EDProducer("IntVecRefToBaseVectorProducer",
    target = cms.string('intvec')
)

process.intvecptrvec = cms.EDProducer("IntVecPtrVectorProducer",
    target = cms.string('intvec')
)

process.ovsimple = cms.EDProducer("OVSimpleProducer",
    size = cms.int32(7)
)

process.simple = cms.EDProducer("SCSimpleProducer",
    size = cms.int32(5)
)

process.vsimple = cms.EDProducer("VSimpleProducer",
    size = cms.int32(7)
)

process.testview = cms.EDAnalyzer("ViewAnalyzer")

process.p = cms.Path(process.simple +
                     process.vsimple +
                     process.ovsimple +
                     # avsimple +
                     process.dsvsimple +
                     process.intvec +
                     process.intlist +
                     process.intdeque +
                     process.intset +
                     process.intvecrefvec +
                     process.intvecreftbvec +
                     process.intvecptrvec)
process.e1 = cms.EndPath(process.testview)
