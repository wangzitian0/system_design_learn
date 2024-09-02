#!/bin/bash

# 获取命令行参数
MODE=$1
SCRIPT_PATH=$2
SCRIPT_NAME=$(basename "$SCRIPT_PATH" .py)
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
RESOLUTION_NAME=""
WIDTH=""
HEIGHT=""
FRAME_RATE=""
OUTPUT_DIR=""
TIMEHASH=$(date +%y%m%d-%H%M%S)  # 自定义时间戳格式为 YYMMDD-HHMMSS

# 根据模式设置渲染配置
if [ "$MODE" == "quick" ]; then
    RESOLUTION_NAME="w540h960p15"
    WIDTH="540"
    HEIGHT="960"
    FRAME_RATE=15
    OUTPUT_DIR="media/$SCRIPT_DIR"
elif [ "$MODE" == "std" ]; then
    RESOLUTION_NAME="w1080h1920p30"
    WIDTH="1080"
    HEIGHT="1920"
    FRAME_RATE=30
    OUTPUT_DIR="media/$SCRIPT_DIR"
elif [ "$MODE" == "release" ]; then
    RESOLUTION_NAME="w1080h1920p30"
    WIDTH="1080"
    HEIGHT="1920"
    FRAME_RATE=30
    OUTPUT_DIR="release/$SCRIPT_DIR"
else
    echo "未知模式: $MODE"
    echo "使用方法: ./build.sh [quick|std|release] <script_path>"
    exit 1
fi

# 确保输出目录存在
mkdir -p "$OUTPUT_DIR"

# 生成输出文件名
OUTPUT_FILE="$SCRIPT_NAME.$RESOLUTION_NAME.$TIMEHASH.mp4"
FINAL_OUTPUT_PATH="$OUTPUT_DIR/$OUTPUT_FILE"

# 运行 Manim 渲染命令
if [ "$MODE" == "release" ]; then
    manim -r ${WIDTH},${HEIGHT} --frame_rate $FRAME_RATE $SCRIPT_PATH -o "$OUTPUT_FILE"
else
    manim -p -r ${WIDTH},${HEIGHT} --frame_rate $FRAME_RATE $SCRIPT_PATH -o "$OUTPUT_FILE"
fi

# 定义正确的搜索路径
SEARCH_DIR="media/videos/$SCRIPT_NAME/${HEIGHT}p$FRAME_RATE"

# 查找生成的文件并移动到最终位置
if [ -f "$SEARCH_DIR/$OUTPUT_FILE" ]; then
    mv "$SEARCH_DIR/$OUTPUT_FILE" "$FINAL_OUTPUT_PATH"
else
    echo "错误：找不到生成的文件 $OUTPUT_FILE"
    exit 1
fi

echo "$MODE 渲染完成: $FINAL_OUTPUT_PATH"