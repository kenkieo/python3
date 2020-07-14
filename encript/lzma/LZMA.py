# LZMA的压缩输出流是一个比特流，
# 采用自适应二进制行程编码器（adaptive binary range coder）。
# 比特流划分为包（packet），
# 每个包或者表示一个字节的被压缩数据，
# 或者如同LZ77的压缩输出序列那样的长度与距离的对（pair）。
# 每个包得每个部分作为独立的上下文（context），
# 从而对每个比特的概率预测仅相关于前一个包的同类型比特值

# 包的比特序列	                包名	        描述
# 0 + byteCode	                LIT	            单个字节，采用自适应二进制行程编码器。
# 1+0 + len + dist	            MATCH	        一个典型的LZ77序列使用长度与距离。
# 1+1+0+0	                    SHORTREP	    单个字节的LZ77序列。距离等于上个LZ77包使用的距离。
# 1+1+0+1 + len	                LONGREP[0]	    单个LZ77序列。距离等于上个LZ77包使用的距离。
# 1+1+1+0 + len	                LONGREP[1]	    单个LZ77序列。距离等于倒数第二个LZ77包使用的距离。
# 1+1+1+1+0 + len	            LONGREP[2]	    单个LZ77序列。距离等于倒数第三个LZ77包使用的距离。
# 1+1+1+1+1 + len	            LONGREP[3]	    单个LZ77序列。距离等于倒数第四个LZ77包使用的距离。

# LONGREP[*] 表示LONGREP[0-3]四种包, *REP指称LONGREP 与SHORTREP, *MATCH指称MATCH或*REP.
# LONGREP[n]包删除了对距离的直接表示，而是使用包序列最近四个距离。

# 包的长度部分表示如下：
#
# 长度比特序列	描述
# 0+ 3 bits	    长度用3比特编码，表示 2 到 9.
# 1+0+ 3 bits	长度用3比特编码，表示 10到17.
# 1+1+ 8 bits	长度用8比特编码，表示 18到273.

# 如同LZ77, 长度不一定要小于距离。
# 距离在逻辑上是32比特，距离0表示最近增加到词典的那个字节。
# 距离的编码以6比特"distance slot"开始，由此可知后面跟着多少比特来补全。这是可变长编码。 距离解码后为比特流，从最显著位到最不显著位。distance slots 0−3直接编码了0−3.


# 6-bit distance slot	                Highest 2 bits	                Fixed 0.5 probability bits	                跟随的比特位数
# 0	                                    00	                            0	                                        0
# 1	                                    01	                            0	                                        0
# 2	                                    10	                            0	                                        0
# 3	                                    11	                            0	                                        0
# 4	                                    10	                            0	                                        1
# 5	                                    11	                            0	                                        1
# 6	                                    10	                            0	                                        2
# 7	                                    11	                            0	                                        2
# 8	                                    10	                            0	                                        3
# 9	                                    11	                            0	                                        3
# 10	                                10	                            0	                                        4
# 11	                                11	                            0	                                        4
# 12	                                10	                            0	                                        5
# 13	                                11	                            0	                                        5
# 14–62 (even)	                        10	                            ((slot / 2) − 5)	                        4
# 15–63 (odd)	                        11	                            (((slot − 1) / 2) − 5)	                    4
