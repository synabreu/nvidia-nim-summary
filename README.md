# nvidia-nim-summary

### NVIDIA NIM (NVIDIA Infrastructure Manager) ###
<p>NVIDIA NIM(NVIDIA Infrastructure Manager)를 처음 듣는 분들에게, 간단히 정리하자면 다음과 같음. NIM은 고성능 컴퓨팅(HPC), AI 워크로드 및 GPU 가속 환경을 위해 NVIDIA 하드웨어 인프라를 간단하고 최적화하여 관리할 수 있도록 설계된 소프트웨어 플랫폼을 말함. 이 플랫폼은 NVIDIA GPU, DGX 시스템 및 네트워킹 구성 요소를 포함한 NVIDIA 시스템의 배포 및 운영을 모니터링, 관리 및 자동화하는 도구를 제공함. 또한, NVIDIA NIM은 대규모 GPU 클러스터 관리를 효율적으로 수행해야 하는 복잡한 AI 및 HPC 워크로드를 실행하는 조직에 특히 유용함. 이 솔루션은 인프라 관리를 간소화하고 자원 활용도를 최적화함으로써 다른 NVIDIA 솔루션을 보완함. </p>

<p>NVIDIA NIM의 주요 기능은 다음과 같다. 
  
<p>* 중앙 집중식 관리: NVIDIA GPU 클러스터와 DGX 시스템을 모니터링하고 관리할 수 있는 통합 인터페이스를 제공함. </p>
<p>* 성능 모니터링: GPU 활용률, 온도, 전력 소비 및 기타 성능 지표를 실시간으로 추적함. </p>
<p>* 자원 최적화: 작업 부하 전반에 걸쳐 GPU 자원의 효율적인 할당과 사용을 보장함. </p>
<p>* 배포 간소화: GPU 가속 환경의 설정 및 배포를 자동화하여 복잡성을 줄여줌. </p>
<p>* 확장성: 데이터 센터 또는 클라우드 환경에서 대규모 멀티 노드 GPU 클러스터 관리를 지원함. </p>
<p>* 통합: NVIDIA AI Enterprise, CUDA와 같은 NVIDIA 소프트웨어 스택 및 Kubernetes와 같은 컨테이너 오케스트레이션 플랫폼과 원활하게 통합됨. </p>
<P>* 알림 및 진단: 시스템 상태를 유지하고 다운타임을 최소화하기 위해 사전 경고 및 진단 기능을 제공함. </P>

### [NVIDIA NIM으로 생성형 AI를 배포하기 위한 빠른 가이드](https://developer.nvidia.com/ko-kr/blog/a-simple-guide-to-deploying-generative-ai-with-nvidia-nim/?ncid=em-anno-720296) ###

### 최신 트렌드 *** 

### [1. 3D Conditioning for Precise Visual Generative AI](https://build.nvidia.com/nvidia/conditioning-for-precise-visual-generative-ai?ncid=em-anno-621294)
<p>요약: [Microsoft Ignite 2024](https://ignite.microsoft.com/en-US/home)에서 발표된 정밀한 시각적 생성형 AI를 위한 3D 컨디셔닝용 Omniverse Blueprint는 개발자가 실시간 렌더링과 생성형 AI 출력을 활용해 브랜드에 부합하는 정확한 마케팅 비주얼을 제작할 수 있는 애플리케이션을 구축할 수 있도록 지원함.</p>

##### [Blog: Building a Generative AI OpenUSD App for Brand-Accurate Marketing Visuals](https://developer.nvidia.com/blog/building-a-generative-ai-openusd-app-for-brand-accurate-marketing-visuals/?ncid=em-anno-706346)

### [2. Build a Digital Twin for Interactive Fluid Simulation](https://build.nvidia.com/nvidia/digital-twins-for-fluid-simulation?ncid=em-anno-769741) 
<p>요약: [수퍼컴퓨팅(SC24)](https://sc24.supercomputing.org/)에서 실시간 컴퓨터 지원 엔지니어링 디지털 트윈을 위한 Omniverse Blueprint를 발표함. 이를 통해 소프트웨어 개발자는 항공우주, 자동차, 제조, 에너지 등 다양한 산업의 컴퓨터 지원 엔지니어링(CAE) 고객들이 실시간 상호작용이 가능한 디지털 트윈을 효과적으로 제작할 수 있도록 지원할 수 있음.</p>

### NVIDIA NIM 자체 호스팅 모범 사례 ###
* [Cordiff](https://build.nvidia.com/nvidia/corrdiff?ncid=em-anno-300376): 지역별 고해상도 기상장을 생성하기 위해 보다 상세한 데이터를 나타내는 생성형 모델임. 
* [FourCastNet](https://build.nvidia.com/nvidia/fourcastnet?ncid=em-anno-513177): FourCastNet은 다양한 날씨/기후 변수의 전 세계 대기 역학을 예측합니다.
* [Llama-3.1 Nemotron 70B-Instruct](https://build.nvidia.com/nvidia/llama-3_1-nemotron-70b-instruct?ncid=em-anno-218061): 거대 언어 모델(LLM)이 더욱 유용한 답변을 생성하도록 향상하기 위해 NVIDIA가 맞춤 조정한 LLM임. 
* [USD Search](https://build.nvidia.com/nvidia/usdsearch?ncid=em-anno-409649): 텍스트 또는 이미지를 입력하면 AI를 기반으로 OpenUSD 데이터, 3D 모델, 이미지, 에셋을 검색함. 

### NVIDIA API 카탈로그에서 무료 크레딧을 사용해 NVIDIA 호스팅 API 엔드포인트를 호출하는 사례 ###

* [Audio2Face 3D](https://build.nvidia.com/nvidia/audio2face-3d?ncid=em-anno-743715): 스트리밍된 오디오를 페이셜 블렌드 셰이프(Blend shape)로 변환하여 실시간 립싱크와 표정 연기를 제공함.
* [Deepfake Image Detection](https://build.nvidia.com/hive/deepfake-image-detection?ncid=em-anno-709972): 얼굴을 감지하여 딥페이크 이미지를 식별하는 고급 AI 모델.
* [Parakeet CTC 0.6b ASR](https://build.nvidia.com/nvidia/parakeet-ctc-0_6b-asr?ncid=em-anno-357672): 최첨단 수준의 정확성과 속도로 영어 전사(transcript)를 제공함.

---------------------------------------------------------------
* [NVIDIA NIM 한글 서비스](https://www.nvidia.com/ko-kr/ai/)
* [NVIDIA NGC - NIM 추론 서비스 셀프 호스팅](https://catalog.ngc.nvidia.com/?filters=nvidia_nim%7CNVIDIA+NIM%7Cnimmcro_nvidia_nim&orderBy=scoreDESC&query=+&page=&pageSize=&ncid=em-anno-211057)
  
