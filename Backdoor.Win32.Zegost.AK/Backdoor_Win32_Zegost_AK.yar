rule Backdoor_Win32_Zegost_AK
{
    meta:
        author = "felicitychou"
        date = "20170220"
        description = "Backdoor:Win32/Zegost.AK(Microsoft)"
    
    strings:
        $s0 = "SynFlood"
        $s1 = "ICMPFlood"
        $s2 = "UDPFlood"
        $s3 = "UDPSmallFlood"
        $s4 = "TCPFlood"
        $s5 = "MultiTCPFlood"
        $s6 = "DNSFlood"
        $s7 = "Game2Flood"
        $s8 = "HTTPGetFlood"
        $s9 = "WebWXCCFlood"
        $s10 = "WebDownFileFlood"
        $s11 = "DIYTCPFlood"
        $s12 = "DIYUDPFlood"
        $s13 = "xq1986"

    condition:
    10 of them
}
