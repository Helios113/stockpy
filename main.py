import segmentTools as sT
import dataConditioning as dC
data = [1, 2, 3, 4, -1, 2, 3, 5]

dat = dC.DataSteam(data)
info = dat.getScroll(20, 1)
t = sT.DataSegment(info, len(info))
t.standardize()
