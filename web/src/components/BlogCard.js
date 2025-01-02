'use client';

import React from 'react';
import { Clock, ChevronRight } from 'lucide-react';

export function BlogCard({ post }) {
  return (
    <article className="bg-white/5 rounded-xl overflow-hidden hover:bg-white/10 transition-colors duration-300">
      <div className="relative aspect-video">
        <img
          src={post.headerImage.src}
          alt={post.headerImage.alt}
          className="w-full h-full object-cover"
          loading="lazy"
        />
        {/* Optional overlay gradient */}
        <div className="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
      </div>
      <div className="p-6">
        <div className="flex items-center gap-4 mb-4">
          <span className="text-pink-400 text-sm">{post.category}</span>
          <div className="flex items-center gap-1 text-pink-100 text-sm">
            <Clock size={14} />
            {post.readTime}
          </div>
        </div>
        <h3 className="text-xl font-bold text-white mb-2">
          {post.title}
        </h3>
        <p className="text-pink-100 mb-4">
          {post.excerpt}
        </p>
        <a 
          href={`/blog/${post.slug}/`}
          className="text-pink-400 hover:text-pink-300 flex items-center gap-1 text-sm font-medium"
        >
          Read More
          <ChevronRight size={16} />
        </a>
      </div>
    </article>
  );
}