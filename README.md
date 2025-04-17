# ModelCheck

## 获取哈希值文件
进入权重文件夹A，通过如下命令获取哈希值文件
`nohup find . -type f -exec sha256sum {} + > hash_list_A.txt 2>&1 &`

进入权重文件夹B，通过如下命令获取哈希值文件
`nohup find . -type f -exec sha256sum {} + > hash_list_B.txt 2>&1 &`

## 比对权重文件夹
通过下面命令进行比对
`python compare_hashes.py hash_list_A.txt hash_list_B.txt`
结果示例如下：

```
Files only in hash_list_A.txt: 0

Files only in hash_list_B.txt: 0

Modified files: 0

Same files: 29
```