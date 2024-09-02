#!/bin/bash

# 获取命令行参数
MODE=$1
SCRIPT_PATH=$2
OUTPUT_DIR="media"  # 默认输出目录
OUTPUT_FILE="output.mp4"  # 生成 .mp4 文件

# 设置根据不同模式生成的配置
if [ "$MODE" == "quick" ]; then
    RESOLUTION="540,960"
    FRAME_RATE=15
    OUTPUT_DIR="media/quick"
elif [ "$MODE" == "std" ]; then
    RESOLUTION="1080,1920"
    FRAME_RATE=30
    OUTPUT_DIR="media/std"
else
    echo "未知模式: $MODE"
    echo "使用方法: ./build.sh [quick|std] <script_path>"
    exit 1
fi

# 确保输出目录存在
mkdir -p $OUTPUT_DIR

# 运行 Manim 渲染命令，生成 mp4 文件并预览
FRAME_RATE=$FRAME_RATE manim -p -r $RESOLUTION $SCRIPT_PATH -o $OUTPUT_FILE --media_dir $OUTPUT_DIR

echo "$MODE 渲染完成: $OUTPUT_DIR/$OUTPUT_FILE"