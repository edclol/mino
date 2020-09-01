# 引入MinIO包。
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

#使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('172.16.1.2:9000',
                    access_key='AKIAIOSFODNN7EXAMPLE',
                    secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                    secure=True)

# minioClient = Minio('play.min.io',
#                     access_key='Q3AM3UQ867SPQQA43P2F',
#                     secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
#                     secure=True)
# 调用make_bucket来创建一个存储桶。
minioClient.make_bucket("edc", location="us-east-1")
minioClient.fput_object('edc', 'hello.go', '/home/edc/hello.go')
minioClient.fput_object('edc', 'kaiji', '/home/edc/kaiji.sh')
try:
    minioClient.make_bucket("edc", location="us-east-1")
except BucketAlreadyOwnedByYou as err:
    pass
except BucketAlreadyExists as err:
    pass
except ResponseError as err:
    pass
else:
    try:
        print("aaa")
        # minioClient.fput_object('edc', '音乐', '/home/edc/音乐')
        minioClient.fput_object('edc', 'hello.go', '/home/edc/hello.go')
        minioClient.fput_object('edc', 'kaiji', '/home/edc/kaiji.sh')
        print("aaa")
    except ResponseError as err:
        print(err)
