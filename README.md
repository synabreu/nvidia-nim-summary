# nvidia-nim-summary

### NVIDIA NIM (NVIDIA Inference Microservice) ###
<p>NVIDIA NIM(NVIDIA Inference Microservice)를 처음 듣는 분들에게, 간단히 정리하자면 다음과 같다. AI 모델의 배포를 가속화하기 위해 설계된 사용하기 쉬운 마이크로서비스 모음이다. 이를 통해 기업은 사내 데이터 센터나 클라우드 환경에서 AI 모델을 효율적으로 배포하고 운영할 수 있다. 따라서, NVIDIA NIM은 AI 모델의 배포를 간소화하고, 확장 가능하며, 보안이 강화된 환경에서 운영할 수 있도록 지원하여 기업의 AI 혁신을 가속화한다.</p>

<p>따라서, 그동안 제가 스터디를 한 내용들을 정리해서 문서와 예제 소스들을 정리해서 현재 [온라인 도서를](https://wikidocs.net/book/17245) 작성하고 있다.</p>

<p>NVIDIA NIM의 주요 특징 다음과 같다.</p> 
  
<p>* 간편한 배포: NIM은 NVIDIA의 최적화된 엔진을 활용하여 AI 모델을 자동으로 컨테이너화하고, NVIDIA 하드웨어에 최적화되어 있다. 그러므로, 이를 통해 수동 설정의 필요성을 없애고 자원 활용의 효율성을 보장한다. </p>
<p>*  </p>
<p>* 확장성: NIM은 온프레미스, 클라우드, 엣지 환경 등 다양한 NVIDIA 플랫폼에서 배포를 관리하고 확장할 수 있어, 변화하는 워크로드와 데이터 요구 사항에 쉽게 적응할 수 있다. </p>
<p>* 모니터링 및 관리: NIM은 모델 성능, 자원 활용도, 상태 등을 모니터링할 수 있는 종합적인 도구를 제공하여, 문제를 신속하게 파악하고 최적의 효율성을 위해 배포를 최적화할 수 있다. </p>
<p>* 보안: NIM은 암호화, 인증, 권한 부여 등을 지원하여 모델과 데이터를 보호하는 강력한 보안 기능을 제공다. </p>
<p>* NVIDIA AI Enterprise 통합: NVIDIA NIM은 NVIDIA AI Enterprise의 일부로, 기업이 AI 모델을 안전하고 효율적으로 배포할 수 있도록 지원한다. 또한, 지속적인 보안 업데이트를 포함한 프로덕션급 런타임을 제공하여 안정적인 API와 엔터프라이즈급 지원을 통해 비즈니스 애플리케이션을 운영할 수 있다. </p>
<P>* RAG 활용: Retrieval-Augmented Generation(RAG)과 같은 기술을 활용하여 AI 모델이 외부 정보를 동적으로 검색하고 활용할 수 있도록 지원한다. 이를 통해 기업은 내부 데이터를 활용하여 AI 모델의 정확성과 신뢰성을 향상시킬 수 있다. </P>

#### [NVIDIA NIM으로 생성형 AI를 배포하기 위한 빠른 가이드](https://developer.nvidia.com/ko-kr/blog/a-simple-guide-to-deploying-generative-ai-with-nvidia-nim/?ncid=em-anno-720296) ####

### 최신 NIM 트렌드 ###

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
  
