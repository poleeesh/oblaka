
## Laboratory work No. 5 "Name"

## The purpose of the work

To get acquainted with the Containerlib tool and methods of working with it, to study the operation of VLAN, IP addressing, etc.

## Progress of work

### Installing prometheus operator:

First we need to install prometheus operator with this command

```
kubectl create -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/master/bundle.yaml

```

The network topology after assembly is shown in the photo below `sudo containerlab deploy networklab.yaml`:  
`sudo containerlab graph`

<img src="./imgs/2.jpg" width=900>

## Configuring the router R01

<img src="./imgs/3.jpg" width=900>

## Configuring SW01.L3.01

<img src="./imgs/4.jpg" width=900>

## Configuring SW02.L3.01

<img src="./imgs/5.jpg" width=900>

## Configuring SW02.L3.02

<img src="./imgs/6.jpg" width=900>

## Checking availability

<img src="./imgs/7.jpg" width=900>

<img src="./imgs/8.jpg" width=900>

## Conclusion

As a result of the laboratory work, we were able to familiarize ourselves with the Containerlib tool, as well as create a network and configure devices based on Linux and RouterOS.